var dynamic_part_names = ['chasis', 'carrosado', 'caja_cambio', 'bomba']

$(function() {
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
