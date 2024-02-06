from django.db import models

from pos.models import Product, Firm
from user.models import User

"""
    Satis siyahisi
"""


class Sale(models.Model):
    employee = models.ForeignKey(User, verbose_name='Satış aparan işçi', on_delete=models.CASCADE)
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
    employee = models.ForeignKey(User, verbose_name='Alan işçi', on_delete=models.CASCADE)
    date = models.DateTimeField('Əməliyyat tarixi', auto_now_add=True)
    quantity = models.FloatField('Say')
    refunded = models.BooleanField(default=False)

    @classmethod
    def get_all_related(cls):
        queryset = cls.objects\
            .select_related('product__measure') \
            .select_related('product__firm') \
            .select_related('employee') \
            .filter(product__is_deleted=False)

        return queryset

    @classmethod
    def get_table_fields(cls):
        arr = ['id', 'refunded']
        fields = [field for field in cls._meta.fields if field.name not in arr]

        return fields


"""
    Firmalara qaytarilan mehsullarin siyahisi
"""


class PurchaseProductRefund(models.Model):
    product = models.ForeignKey(Product, verbose_name='Firmaya qaytarılan məhsul', on_delete=models.CASCADE)
    quantity = models.FloatField('Say')
    employee = models.ForeignKey(User, verbose_name='Geri qaytaran işçi', on_delete=models.CASCADE)
    date = models.DateTimeField('Geri qaytarılma tarixi', auto_now_add=True)
    note = models.TextField('Qeyd', blank=True, null=True)

    @classmethod
    def get_all_related(cls):
        queryset = cls.objects \
            .select_related('product__measure') \
            .select_related('product__firm') \
            .select_related('employee')

        return queryset

    @classmethod
    def get_table_fields(cls):
        arr = ['id']
        fields = [field for field in cls._meta.fields if field.name not in arr]

        return fields
