from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User as CoreUser, AbstractUser

from app.models import DateTimeLog
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
    Istifadeciler: bura daxildir magaza rehberi
    ve magaza iscileri
"""


class User(DateTimeLog, AbstractUser):
    profile_picture = models.ImageField(verbose_name='Profil şəkil', upload_to='images/user', null=True, default='images/user/profilepictures.png')
    is_manager = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'İşçi'
        verbose_name_plural = 'İşçilər'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        return super().save(*args, **kwargs)
