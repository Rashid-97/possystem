from django.forms import ModelForm, ModelChoiceField, Select

from pos.models import Firm, Product


class FirmForm(ModelForm):
    class Meta:
        model = Firm
        fields = ['name', 'phone_number']


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['firm'] = ModelChoiceField(
                                        queryset=Firm.objects.all(),
                                        widget=Select(attrs={'class': 'form-control'}))
        print(self.instance)

    class Meta:
        model = Product
        exclude = ['cdate', 'udate', 'ddate', 'user_create', 'user_update', 'user_delete']
