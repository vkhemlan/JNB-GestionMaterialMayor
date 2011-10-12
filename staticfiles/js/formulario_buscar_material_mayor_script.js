$(function() {    
    $('#id_region').change(function() {
        refresh_cuerpos(false)
    })
    
    refresh_cuerpos(true)
})

function refresh_cuerpos(first_call) {
    var selected_region = parseInt($('#id_region').val())
    var select_cuerpos = $('#id_cuerpo');
    select_cuerpos.empty()
    
    if (selected_region) {
        select_cuerpos.removeAttr('disabled');
        select_cuerpos.append($('<option />').val(0).text('Ver Todos'));
        $.each(window['cuerpos'], function(index, value) {
            if (value[2] == selected_region) {
                select_cuerpos.append($('<option />').val(value[0]).text(value[1]));
            }
        })
        
        if (default_cuerpo != 0 && first_call) {
            select_cuerpos.val(default_cuerpo)
        }
    } else {
        select_cuerpos.append($('<option />').val(0).text('No aplica'));
        select_cuerpos.attr('disabled', true);
    }
}
