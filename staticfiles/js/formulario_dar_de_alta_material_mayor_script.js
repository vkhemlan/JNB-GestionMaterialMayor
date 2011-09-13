var dynamic_part_names = ['chasis', 'carrosado', 'caja_cambio', 'bomba']

$(function() {
    $.each(dynamic_part_names, function(index, value) {
        $('#id_marca_' + value).change(function() {
            generic_refresh(value)
        })
        
        generic_refresh(value)
    })
})

function generic_refresh(part_name) {
    var selected_marca = parseInt($('#id_marca_' + part_name).val())
    var select_modelo = $('#id_modelo_' + part_name);
    select_modelo.empty()
    
    if (selected_marca) {
        select_modelo.removeAttr('disabled');
        $.each(window['modelos_' + part_name], function(index, value) {
            if (value[2] == selected_marca) {
                select_modelo.append($("<option />").val(value[0]).text(value[1]));
            }
        })
    } else {
        select_modelo.append($("<option />").val(0).text('Por favor seleccione una marca'));
        select_modelo.attr('disabled', true);
    }
}
