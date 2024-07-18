from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

from user.models import User


class UserPasswordForm(PasswordChangeForm):
    pass


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            # 'password2'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = self.cleaned_data['password1']
        if commit:
            user.save()
        return user
