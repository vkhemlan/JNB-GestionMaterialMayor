var dynamic_part_names = ['chasis', 'caja_cambio', 'bomba'];

var default_modelos = {}


$(function() {
    $.each(dynamic_part_names, function(index, value) {
        default_modelos[value] = parseInt($('#id_modelo_' + value).val())
        
        $('#id_marca_' + value).change(function() {
            generic_refresh(value, NaN);
        });
        
        generic_refresh(value, default_modelos[value]);
        
        $('#id_modelo_' + value).val(default_modelos[value]);
    });
    
    $('#id_uso').change(function() {
        refresh_otros_usos();
    });
    
    refresh_otros_usos();
    
    $('.required').each(function() {
        $(this).children().append(' (*)');
    });

    $('#id_forma_adquisicion').change(function() {
        refresh_forma_adquisicion();
    });

    refresh_forma_adquisicion();
});

function refresh_forma_adquisicion() {
    selected_forma_adquisicion = $('#id_forma_adquisicion').val();

    var dueno_comodato = $('#id_dueno_comodato');
    var fecha_limitacion_dominio = $('#id_fecha_limitacion_dominio');

    if (selected_forma_adquisicion == 'Donacion') {
        hide_html_element(dueno_comodato);
        show_html_element(fecha_limitacion_dominio);
    } else if (selected_forma_adquisicion == 'Comodato') {
        show_html_element(dueno_comodato);
        hide_html_element(fecha_limitacion_dominio);
    } else {
        hide_html_element(dueno_comodato);
        hide_html_element(fecha_limitacion_dominio);
    }
}

function hide_html_element(elem) {
    elem.parents('tr').hide();
    elem.val('');

    var tr_otros_usos = $(elem.parents()[1]);
    if (tr_otros_usos.prev().attr('class') === 'errorrow') {
        tr_otros_usos.prev().hide();
    }
}

function show_html_element(elem) {
    elem.parents('tr').show();
}

function refresh_otros_usos() {
    var selected_uso = parseInt($('#id_uso').val());
    var select_otros_usos = $('#id_otro_uso');

    if ($.inArray(selected_uso, otros_usos_material_mayor_ids) == -1) {
        hide_html_element(select_otros_usos);
    } else {
        show_html_element(select_otros_usos);
    }
}

function generic_refresh(part_name, default_model_id) {
    var selected_marca = parseInt($('#id_marca_' + part_name).val());
    var select_modelo = $('#id_modelo_' + part_name);
    select_modelo.empty();
    
    if (selected_marca) {
        select_modelo.removeAttr('disabled');
        
        add_another_link = $('#add_id_modelo_' + part_name);
    
        add_another_link.hide();
        
        $.getJSON('/services/part_model_list/', 
            {
                part_name: part_name,
                brand_id: selected_marca
            }, 
            function(data) {
                models = eval(data)
                var max_id = 0;
                var element_added = false;
                $.each(models, function(index, value) {
                    if (value[0] > max_id) {
                        max_id = value[0];
                    }
                    
                    select_modelo.append($("<option />").val(value[0]).text(value[1]));
                    element_added = true;
                })
                
                if (!element_added) {
                    select_modelo.append($("<option />").val(0).text('No hay modelos para esta marca'));
                    select_modelo.attr('disabled', true);
                }
                
                if (default_model_id != NaN) {
                    $('#id_modelo_' + part_name).val(default_model_id);
                } else {
                    $('#id_modelo_' + part_name).val(max_id);
                }
                add_another_link.show();
            }
        );

    } else {
        select_modelo.append($("<option />").val(0).text('Por favor seleccione una marca'));
        select_modelo.attr('disabled', true);
    }
}

function reload_part_model_list(part_name, new_element_id) {
    return
    add_another_link = $('#add_id_modelo_' + part_name);
    
    add_another_link.hide();
    
    $.getJSON('/services/part_model_list/', {
        part_name: part_name
        }, 
        function(data) {
            window['modelos_' + part_name] = eval(data)
            $.each(window['modelos_' + part_name], function(index, value) {
                if (value[0] == new_element_id) {
                    $('#id_marca_' + part_name).val(value[2]);
                    generic_refresh(part_name);
                    return false;
                }
            })
            
            $('#id_modelo_' + part_name).val(new_element_id)
            add_another_link.show()
        }
    );

}



// Handles related-objects functionality: lookup link for raw_id_fields
// and Add Another links.

function html_unescape(text) {
    // Unescape a string that was escaped using django.utils.html.escape.
    text = text.replace(/&lt;/g, '<');
    text = text.replace(/&gt;/g, '>');
    text = text.replace(/&quot;/g, '"');
    text = text.replace(/&#39;/g, "'");
    text = text.replace(/&amp;/g, '&');
    return text;
}

// IE doesn't accept periods or dashes in the window name, but the element IDs
// we use to generate popup window names may contain them, therefore we map them
// to allowed characters in a reversible way so that we can locate the correct 
// element when the popup window is dismissed.
function id_to_windowname(text) {
    text = text.replace(/\./g, '__dot__');
    text = text.replace(/\-/g, '__dash__');
    return text;
}

function windowname_to_id(text) {
    text = text.replace(/__dot__/g, '.');
    text = text.replace(/__dash__/g, '-');
    return text;
}

function showRelatedObjectLookupPopup(triggeringLink) {
    var name = triggeringLink.id.replace(/^lookup_/, '');
    name = id_to_windowname(name);
    var href;
    if (triggeringLink.href.search(/\?/) >= 0) {
        href = triggeringLink.href + '&pop=1';
    } else {
        href = triggeringLink.href + '?pop=1';
    }
    var win = window.open(href, name, 'height=500,width=800,resizable=yes,scrollbars=yes');
    win.focus();
    return false;
}

function dismissRelatedLookupPopup(win, chosenId) {
    var name = windowname_to_id(win.name);
    var elem = document.getElementById(name);
    if (elem.className.indexOf('vManyToManyRawIdAdminField') != -1 && elem.value) {
        elem.value += ',' + chosenId;
    } else {
        document.getElementById(name).value = chosenId;
    }
    win.close();
}

function showAddAnotherPopup(triggeringLink) {
    var name = triggeringLink.id.replace(/^add_/, '');
    name = id_to_windowname(name);
    href = triggeringLink.href
    if (href.indexOf('?') == -1) {
        href += '?_popup=1';
    } else {
        href  += '&_popup=1';
    }
    
    possible_part_name = name.replace('id_modelo_', '')
    if ($.inArray(possible_part_name, dynamic_part_names) != -1) {
        val = $('#id_marca_' + possible_part_name).val()
        href += '&marca=' + val
    }
    
    var win = window.open(href, name, 'height=500,width=800,resizable=yes,scrollbars=yes');
    win.focus();
    return false;
}

function dismissAddAnotherPopup(win, newId, newRepr) {
    // newId and newRepr are expected to have previously been escaped by
    // django.utils.html.escape.
    newId = html_unescape(newId);
    newRepr = html_unescape(newRepr);
    var name = windowname_to_id(win.name);
    var elem = document.getElementById(name);
    
    possible_part_name = name.replace('id_modelo_', '');
    
    if ($.inArray(possible_part_name, dynamic_part_names) != -1) {
        generic_refresh(possible_part_name, parseInt(newId))
    } else if (elem) {
        if (elem.nodeName == 'SELECT') {
            var o = new Option(newRepr, newId);
            elem.options[elem.options.length] = o;
            o.selected = true;
            
            possible_part_name = name.replace('id_marca_', '');
            if ($.inArray(possible_part_name, dynamic_part_names) != -1) {
                generic_refresh(possible_part_name, parseInt(newId))
            }
        } else if (elem.nodeName == 'INPUT') {
            if (elem.className.indexOf('vManyToManyRawIdAdminField') != -1 && elem.value) {
                elem.value += ',' + newId;
            } else {
                elem.value = newId;
            }
        }
    } else {
        var toId = name + "_to";
        elem = document.getElementById(toId);
        var o = new Option(newRepr, newId);
        SelectBox.add_to_cache(toId, o);
        SelectBox.redisplay(toId);
    }
    win.close();
}

