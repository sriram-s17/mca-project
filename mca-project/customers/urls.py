from django.urls import path
from .views import *

urlpatterns = [
    path('', ViewCustomers.as_view(), name='view_customers'),
    path('add/',AddCustomer.as_view(), name='add_customer'),
    path('edit/<int:id>/', EditCustomer.as_view(), name='edit_customer'),
    path('delete/<int:id>/', DeleteCustomer.as_view(), name='delete_customer'),
]