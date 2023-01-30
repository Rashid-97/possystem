from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView

from .forms import UserPasswordForm, UserCreateForm


class UserLogin(LoginView):
    template_name = 'user/login.html'


class UserRegister(CreateView):
    template_name = 'user/register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('user:login')


class UserPasswordChange(PasswordChangeView):
    template_name = 'user/password_change.html'
    form_class = UserPasswordForm
    success_url = reverse_lazy('user:password_change')

    def form_valid(self, form):
        messages.success(self.request, '<div class="alert alert-success" role="alert">Şifrə yeniləndi!</div>')

        return super().form_valid(form)
