$(document).on('click', '.geri_qaytar_btn', function(){
    var product_name = $(this).closest('tr').find('td').eq(1).text();
    var url = $(this).attr('url');

    /* modal part */
    $('#modal_title').text(product_name + ' silinsin?');
    $('#form_modal').attr('action', url)
    $('.modal-body').html('<p><b>Diqqət!</b></p> Məhsullar siyahısından da (məhsulun sayı) silinəcək.');
    $('#modal').find('button[type="submit"]').text('Sil').attr('class', 'btn btn-danger');

});