from django.shortcuts import render, redirect
from django.views import View
from database.forms import *
from django.contrib.auth.decorators import login_required
from user.views import GroupRequiredMixin
from django.contrib.auth.models import Group

# Create your views here.

class ViewWarehouses(GroupRequiredMixin, View):
    groups_required = [group[0] for group in Group.objects.all().values_list("name")]
    def get(self, request):
        context = {
            'warehouses': Warehouse.objects.all()
        }
        return render(request, 'warehouses.html', context)

class AddWarehouse(View):
    def get(self, request):
        return render(request, 'add_warehouse.html', { 'warehouse_form':WarehouseForm })
    
    def post(self, request):
        warehouse_form_data = WarehouseForm(request.POST)
        if warehouse_form_data.is_valid():
            warehouse_form_data.save()
            context = { 'warehouse_form':WarehouseForm, "message":"warehouse added !" }
        else:
            context = { 'warehouse_form':warehouse_form_data }
        return render(request, 'add_warehouse.html', context)

class EditWarehouse(View):
    def get(self, request, id):
        warehouse_obj = Warehouse.objects.get(warehouse_id=id)
        context = {
            'warehouse_form':WarehouseForm(instance=warehouse_obj)
        }
        return render(request, 'edit_warehouse.html', context)
    
    def post(self, request, id):
        warehouse_obj = Warehouse.objects.get(warehouse_id=id)
        warehouse_form_data = WarehouseForm(request.POST, instance=warehouse_obj)
        if warehouse_form_data.is_valid():
            warehouse_form_data.save()
            return redirect("view_warehouses")
        else:
            context = { 'warehouse_form':warehouse_form_data }
            return render(request, 'edit_warehouse.html', context)

class DeleteWarehouse(View):
    def get(request,id):
        warehouse_obj = Warehouse.objects.get(warehouse_id=id)
        warehouse_obj.delete()
        return redirect("view_warehouses")