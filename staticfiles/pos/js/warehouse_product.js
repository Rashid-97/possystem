// qr_scanner();

$(document).on('click', '#delete_product', function(){
    var name = $(this).closest('tr').find('td').eq(0).text();
    var url = $(this).attr('url');

    /* modal part */
    $('#modal_title').text(name + ' silinsin?');
    $('#form_modal').attr('action', url)
    $('.modal-body').html('<p><b>Diqqət!</b></p> Məhsula aid bütün əməliyyatlar silinəcək. <br/><small>Qeyd: məhsullar istənilən zaman bərpa oluna bilər</small>');
    $('#modal').find('button[type="submit"]').text('Sil').attr('class', 'btn btn-danger');

});