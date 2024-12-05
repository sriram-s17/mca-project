from django.shortcuts import render, redirect
from django.views import View
from database.forms import *
from user.views import GroupRequiredMixin

# Create your views here.
class ViewCustomers(GroupRequiredMixin, View):
    groups_required = ['Owner', 'Salesman']
    def get(self, request):
        context = {
            'customers':Customer.objects.all()
        }
        return render(request, 'customers.html', context)

class AddCustomer(GroupRequiredMixin, View):
    groups_required = ['Owner', 'Salesman']
    def get(self, request):
        return render(request, 'add_customer.html', {'customer_form':CustomerForm})

    def post(self, request):
        nextpage = request.GET.get("next", None)
        customer_form_data = CustomerForm(request.POST)
        if customer_form_data.is_valid():
            customer = customer_form_data.save()
            if nextpage=='add_sale':
                return redirect("/sales/add?cid="+str(customer.customer_id))
            context = { 'customer_form':CustomerForm, "message":"customer added !" }
        else:
            context = { 'customer_form':customer_form_data }
        return render(request, 'add_customer.html', context)

class EditCustomer(GroupRequiredMixin, View):
    groups_required = ['Owner', 'Salesman']
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

class DeleteCustomer(GroupRequiredMixin, View):
    groups_required = ['Owner', 'Salesman']
    def get(request, id):
        customer_obj = Customer.objects.get(customer_id = id)
        customer_obj.delete()
        return redirect("view_customers")