from django.db import models

from app.models import Shop


class Firm(models.Model):
    name = models.CharField('Ad', max_length=100)
    phone_number = models.CharField('Əlaqə', max_length=30)
    shop = models.ForeignKey(Shop, verbose_name='Mağaza', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
