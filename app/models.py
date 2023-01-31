from django.db import models

from user.models import User


class UserLog(models.Model):
    user_create = models.ForeignKey(User, verbose_name='Daxil edən', on_delete=models.CASCADE,
                                    related_name='user_creator')
    user_update = models.ForeignKey(User, verbose_name='Dəyişiklik edən', on_delete=models.CASCADE,
                                    related_name='user_update', null=True, blank=True)
    user_delete = models.ForeignKey(User, verbose_name='Silən', on_delete=models.CASCADE, related_name='user_delete',
                                    null=True, blank=True)


class DateTimeLog(models.Model):
    cdate = models.DateTimeField(auto_now_add=True, verbose_name='Yaranma tarixi')
    udate = models.DateTimeField(auto_now=True, verbose_name='Dəyişiklik tarixi')
    ddate = models.DateTimeField(auto_now=True, verbose_name='Silinmə tarixi')

    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ("-cdate",)


class Shop(DateTimeLog):
    name = models.CharField('Mağaza adı', max_length=50, blank=False)
    manager = models.OneToOneField(User, verbose_name='Rəhbər', on_delete=models.CASCADE, related_name='shop')
    unvan = models.TextField(max_length=100)

    def __str__(self):
        return self.name
