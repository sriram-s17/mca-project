from django.urls import path
from .views import *

urlpatterns = [
    path('monthlywise/', MonthlyReport.as_view(), name="monthly_wise_report"),
    path('productwise/', ProductWiseReport.as_view(), name="product_wise_report"),
    path('customerwise/', CustomerWiseReport.as_view(), name="customer_wise_report")
]