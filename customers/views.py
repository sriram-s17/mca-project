from django.shortcuts import render, redirect
from django.views import View
from database.forms import *

# Create your views here.
class ViewCustomers(View):
    def get(self, request):
        context = {
            'customers':Customer.objects.all()
        }
        return render(request, 'customers.html', context)

class AddCustomer(View):
    def get(self, request):
        return render(request, 'add_customer.html', {'customer_form':CustomerForm})

    def post(self, request):
        customer_form_data = CustomerForm(request.POST)
        if customer_form_data.is_valid():
            customer_form_data.save()
            context = { 'customer_form':CustomerForm, "message":"customer added !" }
        else:
            context = { 'customer_form':customer_form_data }
        return render(request, 'add_customer.html', context)

class EditCustomer(View):
    def get(self, request, id):
        customer_obj = Customer.objects.get(customer_id=id)
        context = {
            'customer_form': CustomerForm(instance=customer_obj),
        }
        return render(request, 'edit_customer.html', context)
    
    def post(self, request, id):
        customer_obj = Customer.objects.get(customer_id=id)
        customer_form_data = CustomerForm(request.POST,instance=customer_obj)
        if customer_form_data.is_valid():
            customer_form_data.save()
            return redirect("view_customers")
        else:
            context = { 'customer_form':customer_form_data }
            return render(request, 'edit_customer.html', context)

class DeleteCustomer(View):
    def get(request, id):
        customer_obj = Customer.objects.get(customer_id = id)
        customer_obj.delete()
        return redirect("view_customers")