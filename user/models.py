from django.db import models
from django.contrib.auth.models import User as CoreUser

from app.models import Shop, DateTimeLog


class UserLog(models.Model):
    user_create = models.ForeignKey(CoreUser, verbose_name='Daxil edən', on_delete=models.CASCADE,
                                    related_name='user_creator')
    user_update = models.ForeignKey(CoreUser, verbose_name='Dəyişiklik edən', on_delete=models.CASCADE,
                                    related_name='user_update', null=True, blank=True)
    user_delete = models.ForeignKey(CoreUser, verbose_name='Silən', on_delete=models.CASCADE, related_name='user_delete',
                                    null=True, blank=True)

    class Meta:
        abstract = True


class User(DateTimeLog, CoreUser):
    profile_picture = models.ImageField(upload_to='images/user', null=True, default='images/user/profilepictures.png')
    is_manager = models.BooleanField(default=False)
    shop = models.ManyToManyField(Shop, verbose_name='Mağazalar')

    def __str__(self):
        return self.username
