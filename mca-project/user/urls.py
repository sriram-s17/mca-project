from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('no_permision/', no_permission_page, name="no_permission_page"),
    path('change_password/', ChangePassword.as_view(), name='change_password')
]