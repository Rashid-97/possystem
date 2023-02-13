from django.db import models

from app.models import Shop, DateTimeLog
from user.models import UserLog

"""
    Mehsullarin alindigi firmalar
"""


class Firm(models.Model):
    name = models.CharField('Ad', max_length=100)
    phone_number = models.CharField('Əlaqə', max_length=30)
    shop = models.ForeignKey(Shop, verbose_name='Mağaza', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


"""
    Mehsullarin siyahisi
"""


class Product(UserLog, DateTimeLog):
    name = models.CharField(verbose_name='Məhsulun adı', max_length=100)
    barcode = models.CharField(verbose_name='Barkod', max_length=50, blank=True, null=True)
    picture = models.ImageField(verbose_name='Şəkil', upload_to='images/product', null=True)
    firm = models.ForeignKey(Firm, verbose_name='Firma', on_delete=models.CASCADE)
    price = models.FloatField(verbose_name='Qiymət')
    quantity = models.FloatField(verbose_name='Say')
    measure = models.ForeignKey('UnitOfMeasure', verbose_name='Ölçü vahidi', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


"""
    Olcu vahidleri (meselen: kg, eded ve s.)
"""


class UnitOfMeasure(models.Model):
    measure = models.CharField(verbose_name='Ölçü vahidi', max_length=50)
    abbr = models.CharField(verbose_name='Qısaldılmış adı', max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.abbr + '(' + self.measure + ')'
