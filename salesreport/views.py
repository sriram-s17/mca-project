from django.shortcuts import render, redirect
from django.views import View
from database.models import *

# Create your views here.
class ViewReport1(View):
    def get(self, request):
        context = {
            
        }
        return render(request, "view_report1.html", context)