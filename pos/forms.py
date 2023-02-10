from django.forms import ModelForm

from pos.models import Firm, Product


class FirmForm(ModelForm):
    class Meta:
        model = Firm
        fields = ['name', 'phone_number']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['cdate', 'udate', 'ddate', 'user_create', 'user_update', 'user_delete']
