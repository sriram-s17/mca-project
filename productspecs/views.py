from django.shortcuts import render, redirect
from django.views import View
from database.forms import *
from user.views import GroupRequiredMixin

# Create your views here.
#categories views
class ViewCategories(GroupRequiredMixin, View):
    def get(self, request):
        context = {
            'categories':Category.objects.all()
        }
        return render(request, 'categories.html', context)

class AddCategory(GroupRequiredMixin, View):
    def get(self, request):
        return render(request, 'add_category.html', {'category_form': CategoryForm})
    
    def post(self, request):
        category_form_data = CategoryForm(request.POST)
        if category_form_data.is_valid():
            category_form_data.save()
        return render(request, 'add_category.html', {'category_form': CategoryForm, "message": "Category added!"})

class EditCategory(GroupRequiredMixin, View):
    def get(self, request, id):
        category_obj = Category.objects.get(category_id = id)
        context = {
            'category_form': CategoryForm(instance=category_obj)
        }
        return render(request, 'edit_category.html', context)
    
    def post(self, request, id):
        category_obj = Category.objects.get(category_id = id)
        category_form_data = CategoryForm(request.POST, instance=category_obj)
        if category_form_data.is_valid():
            category_form_data.save()
            return redirect("view_categories")

class DeleteCategory(GroupRequiredMixin, View):
    def get(self, request, id):
        category_obj = Category.objects.get(category_id = id)
        category_obj.delete()
        return redirect("view_categories")


#brands views
class ViewBrands(GroupRequiredMixin, View):
    def get(self, request):
        context = {
            'brands':Brand.objects.all()
        }
        return render(request, 'brands.html', context)

class AddBrand(GroupRequiredMixin, View):
    def get(self, request):
        return render(request, 'add_brand.html', {'brand_form': BrandForm})
    
    def post(self, request):
        brand_form_data = BrandForm(request.POST)
        if brand_form_data.is_valid():
            brand_form_data.save()
        return render(request, 'add_brand.html', {'brand_form': BrandForm, "message":"New Brand added!"})

class EditBrand(GroupRequiredMixin, View):
    def get(self, request, id):
        brand_obj = Brand.objects.get(brand_id = id)
        context = {
            'brand_form': BrandForm(instance=brand_obj)
        }
        return render(request, 'edit_brand.html', context)
    
    def post(self, request, id):
        brand_obj = Brand.objects.get(brand_id = id)
        brand_form_data = BrandForm(request.POST, instance=brand_obj)
        if brand_form_data.is_valid():
            brand_form_data.save()
            return redirect("view_brands")
    

class DeleteBrand(GroupRequiredMixin, View):
    def get(self, request, id):
        brand_obj = Brand.objects.get(brand_id = id)
        brand_obj.delete()
        return redirect("view_brands")


#attributes views
class ViewAttributes(GroupRequiredMixin, View):
    def get(self, request):
        context = {
            'attributes':Attribute.objects.all()
        }
        return render(request, 'attributes.html', context)

class AddAttribute(GroupRequiredMixin, View):
    def get(self, request):
        return render(request, 'add_attribute.html', {'attribute_form': AttributeForm})
    
    def post(self, request):
        attribute_form_data = AttributeForm(request.POST)
        if attribute_form_data.is_valid():
            attribute_form_data.save()
        return render(request, 'add_attribute.html', {'attribute_form': AttributeForm, "message": "Attribute added!"})

class EditAttribute(GroupRequiredMixin, View):
    def get(self, request, id):
        attribute_obj = Attribute.objects.get(attribute_id = id)
        context = {
            'attribute_form': AttributeForm(instance=attribute_obj)
        }
        return render(request, 'edit_attribute.html', context)
    
    def post(self, request, id):
        attribute_obj = Attribute.objects.get(attribute_id = id)
        attribute_form_data = AttributeForm(request.POST, instance=attribute_obj)
        if attribute_form_data.is_valid():
            attribute_form_data.save()
            return redirect("view_attributes")
    
class DeleteAttribute(GroupRequiredMixin, View):
    def get(self, request, id):
        selected_attribute_object = Attribute.objects.get(attribute_id = id)
        selected_attribute_object.delete()
        return redirect("view_attributes")