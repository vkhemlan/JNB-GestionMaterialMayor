$(function() {
    $.datepicker.setDefaults($.datepicker.regional['es']);
    $('.datepicker').datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: 'c-20:c'
    })
})
