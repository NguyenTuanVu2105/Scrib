$(function () {
    $.ajax({
        url: "/json/user",
        dataType: 'json',
        success: function (data) {
            list = data.list;
            $('#user-tags').tagit({
                availableTags: list,
                placeholderText: "Nhập tên",
            });
        }
    })


});