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
    name = models.CharField('Məhsul adı', max_length=100)
    barcode = models.CharField('Barkod', max_length=50, blank=True, null=True)
    picture = models.ImageField('Şəkil', upload_to='images/product', null=True)
    firm = models.ForeignKey(Firm, verbose_name='Firma', on_delete=models.CASCADE)
    price = models.FloatField('Qiymət')
    quantity = models.FloatField('Say')
    measure = models.ForeignKey('UnitOfMeasure', verbose_name='Ölçü vahidi', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


"""
    Olcu vahidleri (meselen: kg, eded ve s.)
"""


class UnitOfMeasure(models.Model):
    measure = models.CharField('Ölçü vahidi', max_length=50)
    abbr = models.CharField('Qısaldılmış adı', max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.abbr + '(' + self.measure + ')'
