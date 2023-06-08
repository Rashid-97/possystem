from django.urls import path

from . import views

app_name = 'pos'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    # path('cash/sale', views.ProductView.as_view(), name='warehouse_products'),
    # path('cash/purchase', views.ProductView.as_view(), name='warehouse_products'),
    path('warehouse/products', views.ProductView.as_view(), name='warehouse_products'),
    path('warehouse/products/create', views.ProductViewCreate.as_view(), name='warehouse_products_create'),
    path('warehouse/unitofmeasure/', views.UnitOfMeasureView.as_view(), name='warehouse_unitofmeasure'),
    path('warehouse/unitofmeasure/create', views.UnitOfMeasureCreateView.as_view(), name='warehouse_unitofmeasure_create'),
    path('warehouse/unitofmeasure/update/<int:pk>', views.UnitOfMeasureUpdateView.as_view(), name='warehouse_unitofmeasure_update'),
    path('warehouse/unitofmeasure/delete/<int:pk>', views.UnitOfMeasureDeleteView.as_view(), name='warehouse_unitofmeasure_delete'),
    path('firm', views.FirmView.as_view(), name='firm'),
    path('firm/create', views.FirmCreateView.as_view(), name='firm_create'),
    path('firm/update/<int:pk>', views.FirmUpdateView.as_view(), name='firm_update'),
    path('firm/delete/<int:pk>', views.FirmDeleteView.as_view(), name='firm_delete'),
    path('employees', views.EmployeeView.as_view(), name='employees'),
    path('employee_block/<int:pk>', views.EmployeeBlockView.as_view(), name='employee_block'),
    path('employee_restore/<int:pk>', views.EmployeeRestoreView.as_view(), name='employee_restore'),
]


