from django.db import models


class DateTimeLog(models.Model):
    cdate = models.DateTimeField(auto_now_add=True, verbose_name='Yaranma tarixi')
    udate = models.DateTimeField(auto_now=True, verbose_name='Dəyişiklik tarixi')
    ddate = models.DateTimeField(auto_now=True, verbose_name='Silinmə tarixi')

    class Meta:
        abstract = True
        ordering = ("-cdate",)


class Shop(DateTimeLog):
    name = models.CharField('Mağaza adı', max_length=50, blank=False)
    unvan = models.TextField('Ünvan', max_length=100)

    def __str__(self):
        return self.name
