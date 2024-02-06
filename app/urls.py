from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('product/<str:pk>', views.check_image_perm, name='check_image_perm')
]
