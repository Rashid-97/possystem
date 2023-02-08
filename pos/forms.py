from django.forms import ModelForm

from pos.models import Firm


class FirmForm(ModelForm):
    class Meta:
        model = Firm
        fields = ['name', 'phone_number']
