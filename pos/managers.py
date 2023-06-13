from django.db import models


class ProductManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()\
            .filter(is_deleted=False)

        return queryset
