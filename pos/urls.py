from django.urls import path

from . import views

app_name = 'pos'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('employees', views.Employee.as_view(), name='employees'),
    path('employee_block/<int:pk>', views.EmployeeBlock.as_view(), name='employee_block'),
    path('employee_restore/<int:pk>', views.EmployeeRestore.as_view(), name='employee_restore')
]
