$(function() {
    $('#id_region_cuerpo_destinatario').change(function() {
        refresh_cuerpo(null)
    });

    refresh_cuerpo(parseInt($('#id_cuerpo_destinatario').val()));
});

function refresh_cuerpo(marked_cuerpo) {
    var select_cuerpo = $('#id_cuerpo_destinatario');
    var selected_region = parseInt($('#id_region_cuerpo_destinatario').val());
    
    select_cuerpo.empty();
    
    if (selected_region) {
        select_cuerpo.removeAttr('disabled');
        $.each(cuerpos, function(index, value) {
            if (value[2] == selected_region) {
                select_cuerpo.append($("<option />").val(value[0]).text(value[1]));
            }
        });
        
        if (marked_cuerpo) {
            select_cuerpo.val(marked_cuerpo)
        }
        
    } else {
        select_cuerpo.append($("<option />").val(0).text('Por favor seleccione una región'));
        select_cuerpo.attr('disabled', true);
    }
}
