from django.forms import ModelForm

from log.models import PurchaseProduct


class PurchaseProductForm(ModelForm):
    class Meta:
        model = PurchaseProduct
        fields = ['product', 'quantity']
