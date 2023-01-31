from django.shortcuts import redirect
from django.urls import resolve

from app import views
from app.services import check_user_for_create_shop
from user.models import User


class AppMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # print('request.user')
        response = self.get_response(request)
        # print('response')
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if resolve(request.path_info).url_name != 'create_shop':
            if request.user.id is not None:  # if user has logged in
                if check_user_for_create_shop(request.user.id):
                    return redirect('app:create_shop')
                else:
                    return None
