$(function() {
	$('.success').slideDown().delay(3000).slideUp();
	$('.error').slideDown().delay(3000).slideUp();
	$('.notice').slideDown().delay(3000).slideUp();

    $('.tablesorter').tablesorter().tablesorterPager({container: $("#pager")});
});
