from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect
from django.views.generic import CreateView

from app.forms import ShopForm
from user.models import User


class CreateShop(LoginRequiredMixin, CreateView):
    template_name = 'app/create_shop.html'
    form_class = ShopForm

    @transaction.atomic
    def form_valid(self, form):
        user_id = self.request.user.id

        form.save()
        shop = form.instance

        user = User.objects.get(pk=user_id)
        user.is_manager = True
        user.shop.add(shop)
        user.save()

        return redirect('pos:home')
