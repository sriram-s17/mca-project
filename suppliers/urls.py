from django.urls import path
from .views import *

urlpatterns = [
    path('', ViewSuppliers.as_view(), name='view_suppliers'),
    path('add/',AddSupplier.as_view(), name='add_supplier'),
    path('edit/<int:id>/', EditSupplier.as_view(), name='edit_supplier'),
    path('delete/<int:id>/', DeleteSupplier.as_view(), name='delete_supplier'),
]