$(function() {
    $('.boton_ejecutar').click(function() {
        var url_form_action = $(this).attr('action');
        $('#formulario_observaciones_ejecucion_mantencion').attr('action', url_form_action);
    });

    $('.boton_posponer').click(function() {
        var url_form_action = $(this).attr('action');
        $('#formulario_observaciones_posponer_mantencion').attr('action', url_form_action);
    });
});