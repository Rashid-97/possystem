from django.db import models
from django.contrib.auth.models import User as CoreUser, AbstractUser

from app.models import Shop, DateTimeLog
from possystem import settings


class UserLog(models.Model):
    user_create = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Daxil edən', on_delete=models.CASCADE,
                                    related_name='user_creator')
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Dəyişiklik edən', on_delete=models.CASCADE,
                                    related_name='user_update', null=True, blank=True)
    user_delete = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Silən', on_delete=models.CASCADE, related_name='user_delete',
                                    null=True, blank=True)

    class Meta:
        abstract = True


"""
    Istifadeciler: bura daxildir magaza rehberleri
    ve magaza iscileri
"""


class User(DateTimeLog, AbstractUser):
    profile_picture = models.ImageField(upload_to='images/user', null=True, default='images/user/profilepictures.png')
    is_manager = models.BooleanField(default=False)
    shop = models.ManyToManyField(Shop, verbose_name='Mağazalar')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username
