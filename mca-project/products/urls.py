from django.urls import path
from .views import *

urlpatterns = [
    
    path('', ViewProducts.as_view(), name='view_products'),
    path('<int:id>/', ViewProduct.as_view(), name='view_product'),
    path('add/', AddProduct.as_view(), name='add_product'),
    path('<int:id>/variant/add', AddVariant.as_view(), name='add_variant'),
    path('edit/<int:id>/', EditProduct.as_view(), name = 'edit_product'),
    path('variant/edit/<int:id>/', EditVariant.as_view(), name = 'edit_variant'),
    path('delete/<int:id>/', DeleteProduct.as_view(), name = 'delete_product'),
    path('variant/delete/<int:id>/', DeleteVariant.as_view(), name = 'delete_variant'),
]