$(function () {
    $('#all_types').click(function () {
        console.log('全部分類');
        var $all_types_container = $("#all_types_container");
        $all_types_container.show();
        var $all_type = $(this);
        var $span = $all_type.find('span').find('span');
        $span.removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up');

        var $sort_rule_container = $('#sort_rule_container')
        $sort_rule_container.slideUp()
        var $sort_rule = $('#sort_rule');
        var $sort_rule_span = $sort_rule.find('span').find('span');
        $sort_rule_span.removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down');
    })

    $('#all_types_container').click(function () {
        var $all_types_container = $(this)
        $all_types_container.hide()
        var $all_type = $('#all_types');
        var $span = $all_type.find('span').find('span');
        $span.removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down');
    })

    $('#sort_rule').click(function () {
        console.log('綜合');
        var $sort_rule_container = $("#sort_rule_container");
        $sort_rule_container.slideDown();
        var $sort_rule = $(this);
        var $span = $sort_rule.find('span').find('span');
        $span.removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up');

        var $all_types_container = $('#all_types_container')
        $all_types_container.hide()
        var $all_type = $('#all_types');
        var $all_type_span = $all_type.find('span').find('span');
        $all_type_span.removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down');
    })

    $('#sort_rule_container').click(function () {
        var $sort_rule_container = $(this)
        $sort_rule_container.slideUp()
        var $sort_rule = $('#sort_rule');
        var $span = $sort_rule.find('span').find('span');
        $span.removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down');
    })

})