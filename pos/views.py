from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from user.models import User


class HomePage(LoginRequiredMixin, ListView):
    template_name = 'pos/home.html'

    def get_queryset(self):
        queryset = {
            'user': User.objects.get(pk=self.request.user.id),
        }

        return queryset

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data()
    #     context['user'] = User.objects.get(pk=self.request.id)
    #     return context
