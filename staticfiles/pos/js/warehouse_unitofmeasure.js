$(document).on('click', '#delete_unitofmeasure', function(){
    var unitofmeasure_name = $(this).closest('tr').find('td').eq(1).find('input').val();
    var url = $(this).attr('url');

    /* modal part */
    $('#modal_title').text(unitofmeasure_name + ' silinsin?');
    $('#form_modal').attr('action', url)
    $('.modal-body').html('<p><b>Diqqət!</b></p> Silinən ölçü vahidinə aid bütün məhsullar da silinəcək.');
    $('#modal').find('button[type="submit"]').text('Sil').attr('class', 'btn btn-danger');

});

// $(document).on('change', '.unitofmeasure_edit_form :input', function() {
//     alert('asdsadsa')
//     $(this).find('button[type="submit"]').prop('disabled', false);
// });