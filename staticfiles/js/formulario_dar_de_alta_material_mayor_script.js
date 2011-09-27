var dynamic_part_names = ['chasis', 'caja_cambio', 'bomba']

$(function() {
    $.each(dynamic_part_names, function(index, value) {
        $('#id_marca_' + value).change(function() {
            generic_refresh(value)
        })
        
        generic_refresh(value)
        
        if (typeof window['default_modelo_' + value] == 'number') {
            $('#id_modelo_' + value).val(window['default_modelo_' + value])
        }
    })

    $.datepicker.setDefaults( $.datepicker.regional['es'] );
    $('.datepicker').datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: 'c-20:c'
    })
})

function generic_refresh(part_name) {
    var selected_marca = parseInt($('#id_marca_' + part_name).val())
    var select_modelo = $('#id_modelo_' + part_name);
    select_modelo.empty()
    
    if (selected_marca) {
        select_modelo.removeAttr('disabled');
        var element_added = false
        $.each(window['modelos_' + part_name], function(index, value) {
            if (value[2] == selected_marca) {
                select_modelo.append($("<option />").val(value[0]).text(value[1]));
                element_added = true
            }
        })
        if (!element_added) {
            select_modelo.append($("<option />").val(0).text('No hay modelos para esta marca'));
            select_modelo.attr('disabled', true);
        }
    } else {
        select_modelo.append($("<option />").val(0).text('Por favor seleccione una marca'));
        select_modelo.attr('disabled', true);
    }
}

function reload_part_model_list(part_name, new_element_id) {
    add_another_link = $('#add_id_modelo_' + part_name)
    
    add_another_link.hide()
    
    $.getJSON('/services/part_model_list/', {
        part_name: part_name
        }, 
        function(data) {
            window['modelos_' + part_name] = eval(data)
            $.each(window['modelos_' + part_name], function(index, value) {
                if (value[0] == new_element_id) {
                    $('#id_marca_' + part_name).val(value[2])
                    generic_refresh(part_name)
                    return false
                }
            })
            
            $('#id_modelo_' + part_name).val(new_element_id)
            add_another_link.show()
        }
    )

}
