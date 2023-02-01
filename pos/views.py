from django.contrib.auth.mixins import LoginRequiredMixin
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

    def get_queryset(self):
        queryset = User.objects.filter(shop=self.request.session.get('curr_shop_id'))
        print
        return queryset
