$("#generate_password").click(function(){
    let randomPassword = Math.random().toString(36).slice(-8);
    $("#inputPassword1").val(randomPassword)

    return false;
});
