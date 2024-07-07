from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import AccessMixin
from database.forms import *

# Create your views here.
class LoginView(View):
    def get(self, request):
        context = {

        }
        
        login_msg = request.GET.get("login")
        if login_msg:
            context['error'] = "Username or Password is wrong"

        return render(request, 'login.html', context)
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        else:
            return redirect('/user/login?login=failed')
        return redirect('home_page')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login_page')

def no_permission_page(request):
    return render(request, "no_permission.html")

class GroupRequiredMixin(AccessMixin):
    groups_required = ['owner']
    
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('login_page')
        if not any([user.groups.filter(name=group).exists() for group in self.groups_required]):
            return self.handle_no_permission()
        return super().dispatch(request,*args, **kwargs)
    
    def handle_no_permission(self):
        return redirect("no_permission_page")
    
class ChangePassword(GroupRequiredMixin, View):
    def get(self, request):
        context = {
            'form': ChangePwdForm
        }
        username = request.GET.get("username", None)
        if username:
            context = {
                'form': ChangePwdForm(initial={'username': username})
            }
        status = request.GET.get("status", None)
        if status:
            if status == "success":
                context["message"] = "Password changed Successfully"
            else:
                context["message"] = request.POST["message"]
        return render(request, 'change_password.html', context)
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.get(username=username)
        if user:
            user.set_password(password)
            user.save()
        else:
            return redirect(f"/user/change_password?username={username}status=error&message=Username is wrong")
        return redirect(f"/user/change_password?username={username}&status=success")
        

