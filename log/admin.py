from django.contrib import admin

from . models import Sale, SaleProduct, SaleProductRefund, PurchaseProduct, PurchaseProductRefund

admin.site.register(Sale)
admin.site.register(SaleProduct)
admin.site.register(SaleProductRefund)
admin.site.register(PurchaseProduct)
admin.site.register(PurchaseProductRefund)
