from pos.models import Product
from user.models import User

"""
    Used for block employees by shop admin
"""


def block_employee(request, **kwargs):
    res = dict()
    res['success'] = False
    try:
        user = User.objects.get(pk=kwargs['pk'])
        user.is_deleted = True
        user.save()
        res['success'] = True
        res['msg'] = "İşçi {user} bloklandı. İşçini istədiyiniz zaman bərpa edə bilərsiniz.".format(user=user)
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
        user.is_deleted = False
        user.save()
        res['success'] = True
        res['msg'] = "İşçi {user} bərpa edildi.".format(user=user)
    except:
        res['msg'] = "İşçi tapılmadı."

    return res


"""
    Product delete (is_deleted column setting True)
"""


def delete_product(pk, user):
    res = dict()
    res['success'] = False
    try:
        product = Product.objects.get(pk=pk)
        product.user_delete = user
        product.is_deleted = True
        product.save()
        res['success'] = True
    except:
        res['msg'] = 'Xəta'

    return res
