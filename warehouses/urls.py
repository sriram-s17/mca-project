from django.urls import path
from .views import *

urlpatterns = [
    path('', ViewWarehouses.as_view(), name='view_warehouses'),
    path('add/', AddWarehouse.as_view(), name='add_warehouse'),
    path('edit/<int:id>/', EditWarehouse.as_view(), name='edit_warehouse'),
    path('delete/<int:id>/', DeleteWarehouse.as_view(), name='delete_warehouse'),
]