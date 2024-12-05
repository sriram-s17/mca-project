from django.shortcuts import render, redirect
from django.views import View
from database.forms import *
from user.views import GroupRequiredMixin

# Create your views here.
class ViewSuppliers(GroupRequiredMixin, View):
    def get(self, request):
        context = {
            'suppliers':Supplier.objects.all()
        }
        return render(request, 'suppliers.html', context)

class AddSupplier(GroupRequiredMixin, View):
    def get(self, request):
        return render(request, 'add_supplier.html', {'supplier_form':SupplierForm})
    
    def post(self, request):
        supplier_form_data = SupplierForm(request.POST)
        if supplier_form_data.is_valid():
            supplier_form_data.save()
            context = { 'supplier_form':SupplierForm, "message":"supplier added !" }
        else:
            context = { 'supplier_form':supplier_form_data }
        return render(request, 'add_supplier.html', context)
    
class EditSupplier(GroupRequiredMixin, View):
    def get(self, request, id):
        supplier_obj = Supplier.objects.get(supplier_id=id)
        context = {
            'supplier_form': SupplierForm(instance=supplier_obj)
        }
        return render(request, 'edit_supplier.html', context)
    
    def post(self, request, id):
        supplier_obj = Supplier.objects.get(supplier_id=id)
        supplier_form_data = SupplierForm(request.POST, instance=supplier_obj)
        if supplier_form_data.is_valid():
            supplier_form_data.save()
            return redirect("view_suppliers")
        else:
            context = { 'supplier_form': supplier_form_data }
            return render(request, 'edit_supplier.html', context)
    
class DeleteSupplier(GroupRequiredMixin, View):
    def get(self, request, id):
        supplier_obj = Supplier.objects.get(supplier_id = id)
        supplier_obj.delete()
        return redirect("view_suppliers")