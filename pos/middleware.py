from django.contrib.auth import logout
from django.shortcuts import redirect

from possystem import settings


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated and request.user.is_deleted:  # if user logged but was deleted by admin
            logout(request)
            return redirect(settings.LOGIN_URL)
