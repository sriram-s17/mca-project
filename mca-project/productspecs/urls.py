from django.urls import path
from .views import *

urlpatterns = [
    path('categories/',ViewCategories.as_view(), name='view_categories'),
    path('categories/add/', AddCategory.as_view(), name='add_category'),
    path('categories/edit/<int:id>/', EditCategory.as_view(), name = 'edit_category'),
    path('categories/delete/<int:id>/', DeleteCategory.as_view(), name = 'delete_category'),
    path('brands/', ViewBrands.as_view(), name='view_brands'),
    path('brands/add/', AddBrand.as_view(), name='add_brand'),
    path('brands/edit/<int:id>/', EditBrand.as_view(), name = 'edit_brand'),
    path('brands/delete/<int:id>/', DeleteBrand.as_view(), name = 'delete_brand'),
    path('attributes/',ViewAttributes.as_view(), name='view_attributes'),
    path('attributes/add/', AddAttribute.as_view(), name='add_attribute'),
    path('attributes/edit/<int:id>/', EditAttribute.as_view(), name = 'edit_attribute'),
    path('attributes/delete/<int:id>/', DeleteAttribute.as_view(), name = 'delete_attribute'),
]