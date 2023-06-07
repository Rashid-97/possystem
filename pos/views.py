from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, ListView

from pos.forms import FirmForm, ProductForm, UnitOfMeasureForm
from pos.mixin import ManagerRequiredMixin
from pos.models import Firm, Product, UnitOfMeasure
from pos.services import block_employee, restore_employee
from user.forms import UserCreateForm
from user.models import User


class HomePage(TemplateView):
    template_name = 'pos/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        user_id = self.request.user.id
        context['user'] = User.objects.filter(pk=user_id)[0]

        return context


class CashSale():
    pass


class CashPurchase():
    pass


class FirmView(CreateView):
    template_name = 'pos/firm.html'
    form_class = FirmForm
    success_url = reverse_lazy('pos:firm')

    def form_valid(self, form):
        messages.success(self.request, 'Firma əlavə edildi.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors, extra_tags='danger')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['firms'] = Firm.objects.all()

        return context


class FirmUpdateView(ManagerRequiredMixin, View):
    def post(self, request, **kwargs):
        firm_form = FirmForm(request.POST)
        if firm_form.is_valid():
            firm_form.save()
            messages.success(request, 'Uğurla yeniləndi.')
        else:
            messages.error(request, 'Xəta.', extra_tags='danger')


class ProductView(ListView):
    template_name = 'pos/warehouse_product.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = Product.get_all_related()
        return queryset


class ProductViewCreate(CreateView):
    template_name = 'pos/warehouse_product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('pos:warehouse_products_create')

    def form_valid(self, form):
        form.instance.user_create_id = self.request.user.id
        messages.success(self.request, 'Məhsul əlavə edildi.')

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors, extra_tags='danger')
        return super().form_invalid(form)


class UnitOfMeasureView(CreateView):
    template_name = 'pos/warehouse_unitofmeasure.html'
    form_class = UnitOfMeasureForm
    context_object_name = 'unitofmeasure'
    success_url = reverse_lazy('pos:warehouse_unitofmeasure_create')

    def form_valid(self, form):
        messages.success(self.request, 'Ölçü vahidi əlavə edildi.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors, extra_tags='danger')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['unitofmeasures'] = UnitOfMeasure.objects.all()

        return context


class EmployeeView(ManagerRequiredMixin, CreateView):
    template_name = 'pos/employee.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('pos:employees')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['employees'] = User.objects.filter(~Q(id=self.request.user.id))

        return context


class EmployeeBlockView(ManagerRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        block_emp = block_employee(request, **kwargs)
        if block_emp['success']:
            messages.success(self.request, block_emp['msg'])
        else:
            messages.error(self.request, block_emp['msg'], extra_tags='danger')

        return redirect('pos:employees')


class EmployeeRestoreView(ManagerRequiredMixin, View):
    def post(self, request, **kwargs):
        restore_emp = restore_employee(request, **kwargs)
        if restore_emp['success']:
            messages.success(self.request, restore_emp['msg'])
        else:
            messages.error(self.request, restore_emp['msg'], extra_tags='danger')

        return redirect('pos:employees')
