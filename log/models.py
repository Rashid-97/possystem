from django.db import models

from pos.models import Product, Firm
from user.models import User

"""
    Satis siyahisi
"""


class Sale(models.Model):
    cashier = models.ForeignKey(User, verbose_name='Kassir', on_delete=models.CASCADE)
    cost = models.FloatField(verbose_name='Qiymət')
    cash_or_card = models.CharField(max_length=4, choices=[
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
    firmalardan alinan mehsullarin siyahisi
"""


class BuyFirm(models.Model):
    firm = models.ForeignKey(Firm, verbose_name='Məhsul alınan firma', on_delete=models.CASCADE)
    employee = models.ForeignKey(User, verbose_name='İşçi', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


"""
    Firmalara qaytarilan mehsullarin siyahisi
"""


class BuyFirmRefundLog(models.Model):
    pass
