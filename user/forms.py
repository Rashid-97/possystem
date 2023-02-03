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
