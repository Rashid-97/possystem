from django.forms import ModelForm, ModelChoiceField, Select

from pos.models import Firm, Product, UnitOfMeasure


class FirmForm(ModelForm):
    class Meta:
        model = Firm
        fields = ['name', 'phone_number']


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.curr_shop_id = kwargs.pop('curr_shop_id', None)
        super().__init__(*args, **kwargs)
        self.fields['firm'] = ModelChoiceField(
            label=Firm._meta.verbose_name,
            queryset=Firm.objects.filter(shop_id=self.curr_shop_id),
            widget=Select(attrs={'class': 'form-control'}))

        self.fields['measure'] = ModelChoiceField(
            label=UnitOfMeasure._meta.verbose_name,
            queryset=UnitOfMeasure.objects.all(),
            widget=Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        exclude = ['cdate', 'udate', 'ddate', 'user_create', 'user_update', 'user_delete']
