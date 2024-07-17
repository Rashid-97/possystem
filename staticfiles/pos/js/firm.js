$(document).on('click', '#delete_firm', function(){
    var firm_name = $(this).closest('tr').find('td').eq(1).find('input').val();
    var url = $(this).attr('url');

    /* modal part */
    $('#modal_title').text(firm_name + ' silinsin?');
    $('#form_modal').attr('action', url)
    $('.modal-body').html('<p><b>Diqqət!</b></p> Silinən firmalara (individual şəxslərə) aid bütün məhsullar da silinəcək.');
    $('#modal').find('button[type="submit"]').text('Sil').attr('class', 'btn btn-danger');

});