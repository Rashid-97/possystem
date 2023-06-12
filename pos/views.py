from django.db import transaction

from django.contrib import messages
from django.db.models import Q, F
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView

from log.forms import PurchaseProductForm
from log.models import PurchaseProduct
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


class FirmView(ListView):
    template_name = 'pos/firm.html'
    queryset = Firm.objects.all()


class FirmCreateView(CreateView):
    model = Firm
    form_class = FirmForm
    success_url = reverse_lazy('pos:firm')

    def form_valid(self, form):
        messages.success(self.request, 'Firma əlavə edildi.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors, extra_tags='danger')
        return super().form_invalid(form)


class FirmUpdateView(ManagerRequiredMixin, UpdateView):
    model = Firm
    form_class = FirmForm
    success_url = reverse_lazy('pos:firm')

    def form_valid(self, form):
        messages.success(self.request, 'Uğurla yeniləndi')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors, extra_tags=['danger'])
        return super().form_invalid(form)


class FirmDeleteView(ManagerRequiredMixin, DeleteView):
    model = Firm
    success_url = reverse_lazy('pos:firm')

    def form_valid(self, form):
        messages.success(self.request, 'Silindi')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors, extra_tags='danger')
        return super().form_invalid(form)


class ProductView(ListView):
    template_name = 'pos/warehouse_product.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = Product.get_all_related()
        return queryset


class ProductCreateView(CreateView):
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


class PurchaseProductView(ListView):
    template_name = 'pos/warehouse_firm_purchase_product.html'
    queryset = PurchaseProduct.get_all_related()
    # paginate = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['products'] = Product.objects.values('id', 'name')

        return context


class PurchaseProductCreateView(CreateView):
    model = PurchaseProduct
    form_class = PurchaseProductForm
    success_url = reverse_lazy('pos:warehouse_firm_purchase')

    def form_valid(self, form):
        try:
            with transaction.atomic():
                form.instance.employee = self.request.user
                response = super().form_valid(form)

                product = Product.objects.get(pk=self.request.POST.get('product'))
                product.quantity = F('quantity') + self.request.POST.get('quantity')
                product.save()

                messages.success(self.request, 'Əməliyyat uğurla yerinə yetirildi')

                return response
        except:
            return 'ERROR'

    def form_invalid(self, form):
        messages.error(self.request, form.errors, extra_tags='danger')
        return super().form_invalid(form)


class UnitOfMeasureView(ListView):
    template_name = 'pos/warehouse_unitofmeasure.html'
    queryset = UnitOfMeasure.objects.all()


class UnitOfMeasureCreateView(CreateView):
    model = UnitOfMeasure
    form_class = UnitOfMeasureForm
    success_url = reverse_lazy('pos:warehouse_unitofmeasure')

    def form_valid(self, form):
        messages.success(self.request, 'Ölçü vahidi əlavə edildi.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors, extra_tags='danger')
        return super().form_invalid(form)


class UnitOfMeasureUpdateView(ManagerRequiredMixin, UpdateView):
    model = UnitOfMeasure
    form_class = UnitOfMeasureForm
    success_url = reverse_lazy('pos:warehouse_unitofmeasure')

    def form_valid(self, form):
        messages.success(self.request, 'Uğurla yeniləndi')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors, extra_tags=['danger'])
        return super().form_invalid(form)


class UnitOfMeasureDeleteView(DeleteView):
    model = UnitOfMeasure
    success_url = reverse_lazy('pos:warehouse_unitofmeasure')

    def form_valid(self, form):
        messages.success(self.request, 'Silindi.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors, extra_tags='danger')
        return super().form_invalid(form)


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
