function postUserList() {
    list = $('.tag');
    userdata = "";
    for (var i=0; i<list.length; i++){
        userdata += list[i].textContent + ", ";
    }
    $('#invite-form').submit(function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: $('#url').text(),
            data: {
                'invited_users' : userdata,
            },
            success: function () {
            }
        });
        return false;
    });
}