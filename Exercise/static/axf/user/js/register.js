$(function () {
    var $username = $('#user_input');
    $username.change(function () {
        var username = $username.val().trim();
        if (username.length) {
            //    帳號預先校驗
            $.getJSON('/axf/check_user/', {'username': username}, function (data) {
                console.log(data);
                var $username_info = $('#username_info');
                if (data['status'] === 200) {
                    $username_info.html('帳號可用').css('color', 'green');
                } else if (data['status'] === 901) {
                    $username_info.html('帳號已存在').css('color', 'red');
                }
            })
        }
    })
    var $email = $('#email_input');
    $email.change(function () {
        var email = $email.val().trim()
        if (email.length) {
            $.getJSON('/axf/check_email/', {'email': email}, function (data) {
                var $email_info = $('#email_info');
                if (data['status'] === 200) {
                    $email_info.html('信箱可以使用').css('color', 'green');
                } else if (data['status'] === 902) {
                    $email_info.html('信箱格式錯誤').css('color', 'red');
                } else if (data['status'] === 903) {
                    $email_info.html('信箱已存在').css('color', 'red');
                }
            })
        }
    })
})

function check() {
    var $username = $('#user_input')
    var username = $username.val().trim();
    if (!username.length) {
        return false
    }
    var info_color = $('#username_info').css('color');
    if (info_color === 'rgb(255, 0, 0)') {
        console.log(info_color);
        return false
    }
    return true
}