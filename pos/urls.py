from django.urls import path

from . import views

app_name = 'pos'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    # path('cash/sale', views.ProductView.as_view(), name='warehouse_products'),
    # path('cash/purchase', views.ProductView.as_view(), name='warehouse_products'),
    path('warehouse/products', views.ProductView.as_view(), name='warehouse_products'),
    path('warehouse/products/create', views.ProductViewCreate.as_view(), name='warehouse_products_create'),
    path('warehouse/unitofmeasure/create', views.UnitOfMeasureView.as_view(), name='warehouse_unitofmeasure_create'),
    path('firm', views.FirmView.as_view(), name='firm'),
    path('firm/update/<int:pk>', views.FirmUpdateView.as_view(), name='firm_update'),
    path('employees', views.EmployeeView.as_view(), name='employees'),
    path('employee_block/<int:pk>', views.EmployeeBlockView.as_view(), name='employee_block'),
    path('employee_restore/<int:pk>', views.EmployeeRestoreView.as_view(), name='employee_restore'),
]


