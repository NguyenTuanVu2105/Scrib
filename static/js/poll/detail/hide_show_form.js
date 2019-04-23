function  HideForm(e) {
    e.preventDefault();
    $('#invite').addClass("hidden");
    $('#btn-add-people').removeClass("hidden");
}

function ShowForm() {
    $('#invite').removeClass("hidden");
    $('#btn-add-people').addClass("hidden");
}