from django.contrib import admin

from pos.models import Firm, Product, UnitOfMeasure

admin.site.register(Firm)
admin.site.register(Product)
admin.site.register(UnitOfMeasure)
