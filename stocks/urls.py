from django.urls import path
from .views import *

urlpatterns = [
    path("", ViewStocks.as_view(), name='view_stocks'),
    path("products/quantity/", get_quantity, name='get_quantity'),
    path("edit/", EditStock.as_view(), name='edit_stock'),
    path("transfer/", TransferStock.as_view(), name='transfer_stock'),
    path("products/warehouseandquantity/", get_warehouse_and_quantity, name="get_warehouse_and_quantity")
]