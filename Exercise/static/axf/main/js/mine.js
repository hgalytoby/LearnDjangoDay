$(function () {
    $('#not_login').click(function () {
        window.open('/axf/login/', '_self');
    })

    $('#regis').click(function () {
        window.open ("/axf/register/", "_self")
        // window.open ("/axf/register/", "newwindow", "height=800, width=800, top=0, left=0, toolbar=no, menubar=no, scrollbars=no, resizable=no,location=no, status=no")
    })
    
})