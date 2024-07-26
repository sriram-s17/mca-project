from django.urls import path
from .views import *

urlpatterns = [
    path('', ViewSales.as_view(), name="view_sales"),
    path('<int:id>/', ViewSale.as_view(), name="view_sale"),
    path('add/', AddSale.as_view(), name="add_sale"),
    path('<int:id>/recordpayment/', RecordPayment.as_view(), name="add_sale_payment"),
]