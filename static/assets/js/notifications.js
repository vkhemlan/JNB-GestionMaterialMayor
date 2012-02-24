$(function() {
	$('.success').slideDown().delay(3000).slideUp();
	$('.error').slideDown().delay(3000).slideUp();
	$('.notice').slideDown().delay(3000).slideUp();

    $('.tablesorter').tablesorter()
    .tablesorterPager({container: $("#pager")})
    .tablesorterFilter({filterContainer: "#filter-box",
                            filterClearContainer: "#filter-clear-button",
                            filterColumns: [0,1,2,3,4,5,6,7]});
});
