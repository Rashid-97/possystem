from django.contrib import admin

from pos.models import Firm, Log, Product

admin.site.register(Firm)
admin.site.register(Product)
admin.site.register(Log)
