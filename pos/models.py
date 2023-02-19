from django.db import models

from app.models import Shop, DateTimeLog
from user.models import UserLog

"""
    Mehsullarin alindigi firmalar
"""


class Firm(models.Model):
    name = models.CharField('Ad', max_length=100)
    phone_number = models.CharField('Əlaqə', max_length=30)
    email = models.EmailField('E-Poçta', max_length=50, blank=True, null=True)
    shop = models.ForeignKey(Shop, verbose_name='Mağaza', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Firma və ya individual şəxs'
        verbose_name_plural = 'Firmalar və ya individual şəxslər'


"""
    Mehsullarin siyahisi
"""


class Product(UserLog, DateTimeLog):
    name = models.CharField(verbose_name='Məhsulun adı', max_length=100)
    barcode = models.CharField(verbose_name='Barkod', max_length=50, blank=True, null=True)
    picture = models.ImageField(verbose_name='Şəkil', upload_to='images/product', blank=True, null=True)
    firm = models.ForeignKey(Firm, verbose_name=Firm._meta.verbose_name, on_delete=models.CASCADE)
    price = models.FloatField(verbose_name='Qiymət')
    quantity = models.FloatField(verbose_name='Say')
    measure = models.ForeignKey('UnitOfMeasure', verbose_name='Ölçü vahidi', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Məhsul'
        verbose_name_plural = 'Məhsullar'


"""
    Olcu vahidleri (meselen: kg, eded ve s.)
"""


class UnitOfMeasure(models.Model):
    measure = models.CharField(verbose_name='Ölçü vahidi', max_length=50)
    abbr = models.CharField(verbose_name='Qısaldılmış adı', max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.abbr + ' (' + self.measure + ')'

    class Meta:
        verbose_name = 'Ölçü vahidi'
        verbose_name_plural = 'Ölçü vahidi'
