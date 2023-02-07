$("#generate_password").click(function (){
    let randomPassword = Math.random().toString(36).slice(-8);
    $("#inputPassword1").val(randomPassword)

    return false;
});

$(document).on('click', "#employee_delete_btn", function (){
    let url = $(this).attr("url");
    let emp_username = $(this).closest('tr').find(".emp_username").text()
    $("#modal_title_employee_delete").text(emp_username+' işçi bloklansın?');
    $("#form_modal_employee_delete").attr("action", url);
});

$(document).on('click', "#employee_restore_btn", function (){
    let url = $(this).attr("url");
    let emp_username = $(this).closest('tr').find(".emp_username").text()
    $("#modal_title_employee_restore").text(emp_username+' bərpa edilsin?');
    $("#form_modal_employee_restore").attr("action", url);
});