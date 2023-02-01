from django.urls import path

from . import views

app_name = 'pos'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('employees', views.Employee.as_view(), name='employees')
]
