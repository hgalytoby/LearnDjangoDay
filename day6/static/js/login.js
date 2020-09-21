$(function () {
    $('img').click(function () {
        console.log('點到了');
        $(this).attr('src', '/app/get_code/?t=' + Math.random())
    })
})