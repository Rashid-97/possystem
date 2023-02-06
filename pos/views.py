from django.contrib import messages
from django.db import transaction
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView, UpdateView, DeleteView

from user.forms import UserCreateForm
from user.models import User


class HomePage(TemplateView):
    template_name = 'pos/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        user_id = self.request.user.id
        context['user'] = User.objects.filter(pk=user_id)[0]

        return context


class Employee(CreateView):
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
        context['employees'] = User.objects.filter(Q(shop=self.request.session.get('curr_shop_id'))
                                                   & ~Q(id=self.request.user.id)
                                                   & Q(is_deleted=False))

        return context


class EmployeeDelete(DeleteView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=kwargs['pk'])
        if user:
            user = user[0]
            if user.shop.all()[0].id == request.session['curr_shop_id']:  # if user's shop id equals to admin's shop id
                User.delete(user_id=kwargs['pk'])
                messages.success(self.request, "İşçi {user} bloklandı. İşçini istədiyiniz zaman bərpa edə bilərsiniz.".format(user=user))
            else:
                messages.success(self.request, "{user} bu mağazanın işçisi deyil.".format(user=user))
        else:
            messages.success(self.request, "İşçi tapılmadı.")

        return redirect('pos:employees')
