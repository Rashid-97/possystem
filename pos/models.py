from django.db import models

from app.models import DateTimeLog
from pos.managers import ProductManager
from user.models import UserLog

"""
    Mehsullarin alindigi firmalar
"""


class Firm(models.Model):
    name = models.CharField('Ad', max_length=100)
    contact = models.CharField('Əlaqə(tel. nömrəsi, e-poçta və s.)', max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Firma və ya individual şəxs'
        verbose_name_plural = 'Firmalar və ya individual şəxslər'


"""
    Mehsullarin siyahisi
"""


class Product(UserLog, DateTimeLog):
    name = models.CharField(verbose_name='Məhsulun adı', max_length=100, unique=True)
    barcode = models.CharField(verbose_name='Barkod', max_length=50, blank=True, null=True, unique=True)
    picture = models.ImageField(verbose_name='Şəkil', upload_to='images/product', blank=True, null=True)
    firm = models.ForeignKey(Firm, verbose_name=Firm._meta.verbose_name, on_delete=models.CASCADE)
    price = models.FloatField(verbose_name='Satış qiyməti (AZN)')
    purchase_price = models.FloatField(verbose_name='Alış qiyməti (AZN)')
    quantity = models.FloatField(verbose_name='Say/Miqdar')
    measure = models.ForeignKey('UnitOfMeasure', verbose_name='Ölçü vahidi', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    objects = ProductManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Məhsul'
        verbose_name_plural = 'Məhsullar'

    @classmethod
    def get_all_related(cls):
        queryset = cls.objects \
            .select_related('firm') \
            .select_related('measure')\

        return queryset


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
