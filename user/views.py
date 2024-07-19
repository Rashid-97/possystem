from django.contrib.auth import login
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, TemplateView

from .forms import UserPasswordForm, UserCreateForm


class UserProfile(TemplateView):
    template_name = 'user/profile.html'


class UserLogin(LoginView):
    template_name = 'user/login.html'

    def form_valid(self, form):
        if not form.get_user().is_deleted:
            login(self.request, form.get_user())
            return super().form_valid(form)
        else:
            form.add_error(None, 'Hesabınız passiv edilmişdir.'
                                 ' Hesabınızın aktivləşdirilməsi üçün mağaza sahibinə müraciət edin.')

            return render(self.request, self.get_template_names(), {'form': form})


class UserRegister(CreateView):
    template_name = 'user/register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('user:login')


class UserPasswordChange(PasswordChangeView):
    template_name = 'user/profile.html'
    form_class = UserPasswordForm
    success_url = reverse_lazy('user:profile')

    def get(self, request, *args, **kwargs):
        print('qqq')
        # Возвращаем ошибку 405 для GET запросов
        return HttpResponseNotAllowed(['POST'])

    def form_valid(self, form):
        print('asd')
        messages.success(self.request, 'Şifrə yeniləndi!')

        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors
        for field, error_list in errors.items():
            label = form.fields[field].label
            for error in error_list:
                messages.error(self.request, f'{label}: {error}', extra_tags='danger')
        return super().form_invalid(form)
