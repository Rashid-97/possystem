from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from user.forms import UserCreateForm
from user.models import User


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'pos/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        user_id = self.request.user.id
        context['user'] = User.objects.filter(pk=user_id)[0]

        return context


class Employee(LoginRequiredMixin, CreateView):
    template_name = 'pos/employee.html'
    form_class = UserCreateForm
    context_object_name = 'employees'
    success_url = reverse_lazy('pos:employees')

    @transaction.atomic
    def form_valid(self, form):
        form.save()
        form.instance.shop.add(self.request.session.get('curr_shop_id'))

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['employees'] = User.objects.filter(Q(shop=self.request.session.get('curr_shop_id')) & ~Q(id=self.request.user.id))

        return context
