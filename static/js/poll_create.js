// var new_author_element=$('#new_author_html');
// var new_author_html=new_author_element.html();
// new_author_element.remove();
// var authorArray=new Array2d([{name:'authors',attributes:['name','email','organize_name']}]);
// function addAuthor(){var target=$('#add-author-before-me');
// target.before(new_author_html);target.prev().slideDown("\fast\");target.prev().find('input[name=\"names[]\"]').focus();initRemoveBtn();authorArray.update();}function initRemoveBtn(){$('.author-remove').click(function(){var target=$(this).parent().parent();target.slideUp(\"fast\",function(){target.remove();authorArray.update();});})}" +
// "$('#form').submit(function(){bootbox.dialog({message:'<p><i class=\"fa fa-spin fa-spinner\"></i> Đang xử lý...</p>'});});initRemoveBtn();authorArray.update();"
//


function addPoll() {
    var new_poll_html = $('#new_poll').html();
    $('#add-time-before-me').before(new_poll_html);
    removeTime();
    addDatePicker();
    addTimePicker();

};

function removeTime() {
    $('.time-remove').click(function () {
        $(this).parent().parent().remove();
    })
}

function addTimePicker() {
         $(document).on('focus','.timepicker', function(){
                          $(this).removeClass('hasDatepicker').timepicker();
                       });
}

function addDatePicker() {
     $(document).on('focus','.datepicker', function(){
                          //$(this).datepicker();
                          $(this).removeClass('hasDatepicker').datepicker();
                       });
}
