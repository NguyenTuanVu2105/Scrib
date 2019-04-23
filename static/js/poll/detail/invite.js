function postUserList() {
    list = $('.tagit-label');
    console.log(list.length);
    userdata = "";
    for (var i=0; i<list.length; i++){
        if (i === list.length - 1)
            userdata += list[i].textContent;
        else
            userdata += list[i].textContent + ", ";
    }
    $.ajax({
            type: "POST",
            url: $('#url').text(),
            data: {
                'users_invited' : userdata,
            },
            success: function () {
                alert("Mời thành công");
                HideForm(event);
            }
        });

}