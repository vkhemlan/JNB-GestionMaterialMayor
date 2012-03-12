$(function() {
    $('#id_motivo').change(function() {
        refresh_motivo();
    });

    refresh_motivo();
});

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

function refresh_motivo() {
    var selected_motivo = $('#id_motivo option:selected').text();
    var select_otros_motivos = $('#id_otro_motivo');

    if (selected_motivo === 'Otro') {
        show_html_element(select_otros_motivos);
    } else {
        hide_html_element(select_otros_motivos);
    }
}
