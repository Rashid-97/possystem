from django.forms import ModelForm

from app.models import Shop


class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = [
            'name',
            'unvan'
        ]
