from user.models import User


"""
    checking if user is manager or belongs to one of the managers
    if none of them then user must create a shop
"""


def check_user_for_create_shop(user_id):
    user = User.objects.prefetch_related('shop').filter(pk=user_id)
    if user:
        user = user[0]
        if user.is_superuser:
            return False
        if user.is_manager:  # if user is manager it means that user has a shop
            return False
        else:
            if user.shop.all():  # if user has a manager so user doesn't need to create a shop
                return False
        return True
    return False
