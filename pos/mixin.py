from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class ManagerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

    def get_redirect_url(self):
        return reverse_lazy('pos:home')

    def handle_no_permission(self):
        return HttpResponseRedirect(self.get_redirect_url())

    def test_func(self):
        return self.request.user.is_manager
