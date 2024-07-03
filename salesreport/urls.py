from django.urls import path
from .views import *

urlpatterns = [
    path('', ViewReport1.as_view(), name="view_report1")
]