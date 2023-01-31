from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView

from app.forms import ShopForm
from user.models import User


class CreateShop(LoginRequiredMixin, CreateView):
    template_name = 'app/create_shop.html'
    form_class = ShopForm
    success_url = reverse_lazy('pos:home')

    @transaction.atomic
    def form_valid(self, form):
        user_id = self.request.user.id
        form.instance.manager_id = user_id

        User.objects.filter(pk=user_id).update(is_manager=True)
        return super().form_valid(form)
