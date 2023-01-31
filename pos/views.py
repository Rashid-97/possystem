from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from user.models import User


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'pos/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        user_id = self.request.user.id
        context['user'] = User.objects.prefetch_related('shop').filter(pk=user_id)[0]

        return context
