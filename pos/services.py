from user.models import User

"""
    Used for block employees by shop admin
"""


def block_employee(request, **kwargs):
    res = dict()
    res['success'] = False
    try:
        user = User.objects.get(pk=kwargs['pk'])
        if user.shop.all()[0].id == request.session['curr_shop_id']:  # if user's shop id equals to admin's shop id
            user.is_deleted = True
            user.save()
            res['success'] = True
            res['msg'] = "İşçi {user} bloklandı. İşçini istədiyiniz zaman bərpa edə bilərsiniz.".format(user=user)
        else:
            res['msg'] = "İşçi tapılmadı."
    except:
        res['msg'] = "İşçi tapılmadı."

    return res


"""
    Used for restoring employees by shop admin
"""


def restore_employee(request, **kwargs):
    res = dict()
    res['success'] = False
    try:
        user = User.objects.get(pk=kwargs['pk'])
        if user.shop.all()[0].id == request.session['curr_shop_id']:  # if user's shop id equals to admin's shop id
            user.is_deleted = False
            user.save()
            res['success'] = True
            res['msg'] = "İşçi {user} bərpa edildi.".format(user=user)
        else:
            res['msg'] = "İşçi tapılmadı."
    except:
        res['msg'] = "İşçi tapılmadı."

    return res
