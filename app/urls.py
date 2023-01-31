from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('create_shop', views.CreateShop.as_view(), name='create_shop'),
]