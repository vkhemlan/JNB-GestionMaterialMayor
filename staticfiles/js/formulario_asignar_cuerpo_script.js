$(function() {    
    $('#id_region').change(function() {
        refresh_cuerpos(null, null)
    })
    
    $('#id_cuerpo').change(function() {
        refresh_companias(null)
    })
    
    $('#id_region').val(default_region_id)
    refresh_cuerpos(default_cuerpo_id, default_compania_id)
})

function refresh_cuerpos(default_cuerpo_id, default_compania_id) {
    var selected_region = parseInt($('#id_region').val())
    var select_cuerpos = $('#id_cuerpo');
    select_cuerpos.empty()
    
    if (selected_region) {
        select_cuerpos.removeAttr('disabled');
        $.each(window['cuerpos'], function(index, value) {
            if (value[2] == selected_region) {
                select_cuerpos.append($('<option />').val(value[0]).text(value[1]));
            }
        })
    } else {
        select_cuerpos.append($('<option />').val(0).text('Por favor seleccione una región'));
        select_cuerpos.attr('disabled', true);
    }
    
    if (default_cuerpo_id) {
        select_cuerpos.val(default_cuerpo_id)
    }
    
    refresh_companias(default_compania_id)
}

function refresh_companias(default_compania_id) {
    var selected_cuerpo = parseInt($('#id_cuerpo').val())
    var select_companias = $('#id_compania');
    select_companias.empty()
    
    select_companias.append($('<option />').val('').text('Nivel central del cuerpo'));
    $.each(companias, function(index, value) {
        if (value[2] == selected_cuerpo) {
            select_companias.append($('<option />').val(value[0]).text(value[1]));
        }
    })
    
    if (default_compania_id) {
        select_companias.val(default_compania_id)
    }
}
