from django.urls import path

from . import views

app_name = 'pos'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('employees', views.Employee.as_view(), name='employees'),
    path('employee_delete/<int:pk>', views.EmployeeDelete.as_view(), name='employee_delete')
]
