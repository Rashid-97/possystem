from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

from user.models import User


class UserPasswordForm(PasswordChangeForm):
    pass


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        ]
