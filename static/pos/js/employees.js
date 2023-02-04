$("#generate_password").click(function (){
    let randomPassword = Math.random().toString(36).slice(-8);
    $("#inputPassword1").val(randomPassword)

    return false;
});

$("#employee_delete_btn").click(function (e){
    let url = $(this).attr("url");
    let emp_username = $(this).closest('tr').find(".emp_username").text()
    let title_text = $("#delete_modal_title").text();
    $("#delete_modal_title").text(emp_username+' '+title_text);
    $("#form_delete").attr("action", url);
});