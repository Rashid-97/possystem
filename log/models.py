from django.db import models

from pos.models import Product, Firm
from user.models import User

"""
    Satis siyahisi
"""


class Sale(models.Model):
    employee = models.ForeignKey(User, verbose_name='İşçi', on_delete=models.CASCADE)
    cost = models.FloatField('Qiymət')
    cash_or_card = models.CharField('Ödəniş növü', max_length=4, choices=[
        ('cash', 'Nağd'),
        ('card', 'Kart')
    ])
    date = models.DateTimeField('Satış tarixi', auto_now_add=True)


"""
    Satilan mehsullarin siyahisi
"""


class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, verbose_name='Satış əməliyyat nömrəsi', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Satılan məhsul', on_delete=models.CASCADE)


"""
    Geri qaytarilan mehsullarin siyahisi
"""


class SaleProductRefund(models.Model):
    sale_product = models.ForeignKey(SaleProduct, verbose_name='Sale Product ID', on_delete=models.CASCADE)
    date = models.DateTimeField('Qaytarılma tarixi', auto_now_add=True)
    note = models.TextField('Qeyd', blank=True, null=True)


"""
    Firmalardan alinan mehsullarin siyahisi
"""


class PurchaseProduct(models.Model):
    product = models.ForeignKey(Product, verbose_name='Alınan məhsul', on_delete=models.CASCADE)
    employee = models.ForeignKey(User, verbose_name='İşçi', on_delete=models.CASCADE)
    date = models.DateTimeField('Alış tarixi', auto_now_add=True)
    quantity = models.FloatField('Say')


"""
    Firmalara qaytarilan mehsullarin siyahisi
"""


class PurchaseProductRefundLog(models.Model):
    product = models.ForeignKey(Product, verbose_name='Firmaya qaytarılan məhsul', on_delete=models.CASCADE)
    quantity = models.FloatField('Say')
    employee = models.ForeignKey(User, verbose_name='İşçi', on_delete=models.CASCADE)
    date = models.DateTimeField('Geri qaytarma tarixi', auto_now_add=True)
    note = models.TextField('Qeyd', blank=True, null=True)
