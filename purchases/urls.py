from django.urls import path
from .views import *

urlpatterns = [
    path('', ViewPurchases.as_view(), name="view_purchases"),
    path('add/', AddPurchase.as_view(), name='add_purchase'),
    path('<int:id>/recordpayment/', RecordPayment.as_view(), name="add_payment"),
    path('<int:id>/', ViewPurchaseDetail.as_view(), name="view_purchase"),
]