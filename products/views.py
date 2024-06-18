from django.shortcuts import render, redirect
from django.views import View
from database.forms import *
import os
from json import dumps
from django.forms import inlineformset_factory
import pprint
# Create your views here.

#products views
class ViewProducts(View):
    def get(self, request):
        products = Product.objects.all()
        product_list = []
        for product in products:
            product_list.append({"product_id":product.product_id, "product_name":product.product_name, "category_ref":product.category_ref, "brand_ref":product.brand_ref, "has_variants":product.has_variants})
        
        for product in product_list:
            if product["has_variants"] == True:
                variants = ProductVariant.objects.filter(product_ref=product["product_id"])
                variant_list = []
                for variant in variants:
                    product_detail = ProductDetail.objects.get(variant_ref = variant.variant_id)
                    var_attr_values = VariantAttributeValue.objects.filter(variant_ref = variant.variant_id)
                    var_attr_value_list = []
                    for attr_value in var_attr_values:
                        var_attr_value_list.append({"attribute_ref":attr_value.attribute_ref, "value":attr_value.value})
                    
                    variant_detail = {"variant_id":variant.variant_id, "variant_name":variant.variant_name, "product_code":product_detail.product_code, "product_image":product_detail.product_image, "selling_price":product_detail.selling_price, "is_active":product_detail.is_active, "attributes":var_attr_value_list}
                    variant_list.append(variant_detail)
                product.update({"variants":variant_list})
            else:
                product_detail = ProductDetail.objects.get(product_ref = product["product_id"])
                product.update({"product_code":product_detail.product_code, "product_image":product_detail.product_image, "selling_price":product_detail.selling_price, "is_active":product_detail.is_active})
        
        context = {
            "products":product_list
        }
        return render(request, 'products.html', context)
    
# class ViewProduct(View):
#     def get(self, request, id):
#         product = Product.objects.get(product_id=id)
#         product_dict = {"product_id":product.product_id, "product_name": product.product_name,
#                         "category_ref": product.category_ref, "brand_ref": product.brand_ref,
#                         "description":product.description, "has_variants":product.has_variants}
        
#         if product_dict["has_variants"]:
#             variants = ProductVariant.objects.filter(product_ref=product_dict["product_id"])
#             variants_list = []
#             if variants:
#                 for variant in variants:
#                     variant_dict = {"variant_id": variant.variant_id, "variant_name":variant.variant_name}
                    
#                     var_attr_values = VariantAttributeValue.objects.filter(variant_ref=variant)
#                     attr_values_list = []
#                     for attr_value in var_attr_values:
#                         attr_values_list.append({"attribute":attr_value.attribute_ref, "value":attr_value.value})
#                     variant_dict.update({"attr_values":attr_values_list})
                    
#                     product_detail = ProductDetail.objects.filter(variant_ref=variant)[0]
#                     variant_dict.update({"product_detail_id":product_detail.product_detail_id, "product_code":product_detail.product_code, 
#                                  "product_image":product_detail.product_image, "selling_price":product_detail.selling_price, 
#                                  "low_stock_threshold": product_detail.low_stock_threshold, "is_active":product_detail.is_active})

#                     stock = StockDetail.objects.filter(product_detail_ref = product_detail)
#                     if stock:
#                         stock = stock[0]
#                         variant_dict.update({"quantity": stock.quantity})
                    
#                     variants_list.append(variant_dict)
#                 product_dict.update({"variants":variants_list})
#         else:
#             product_detail = ProductDetail.objects.filter(product_ref=product_dict["product_id"])[0]
#             product_dict.update({"product_detail_id":product_detail.product_detail_id, "product_code":product_detail.product_code, 
#                                  "product_image":product_detail.product_image, "selling_price":product_detail.selling_price, 
#                                  "low_stock_threshold": product_detail.low_stock_threshold, "is_active":product_detail.is_active})
            
#             stock = StockDetail.objects.filter(product_detail_ref = product_detail)[0]
#             if stock:
#                 product_dict.update({"quantity": stock.quantity})
        
#         return render(request, "view_product.html", {"product":product_dict})

# class AddProduct(View):
#     def get(self, request):
#         return render(request, 'add_product.html', {'product_form': ProductForm, 'detail_form': ProductDetailForm} )
    
#     def post(self, request):
#         product_form_data = ProductForm(request.POST)
#         if product_form_data.is_valid():
#             product = product_form_data.save()
#             if not product.has_variants:
#                 detail_form_data = ProductDetailForm(request.POST, request.FILES)
#                 detail = detail_form_data.save(commit=False)
#                 detail.product_ref = product
#                 detail.save()
#                 return render(request, 'add_product.html', {'product_form': ProductForm, 'detail_form': ProductDetailForm, "message":"product added ! "} )
#             else:
#                 return redirect('add_variant', product.product_id)

# class AddVariant(View):
#     def get(self, request, id):
#         variantcount = ProductVariant.objects.filter(product_ref=id).count()
#         product = Product.objects.get(product_id = id)
#         context = {
#             'variant_form': VariantForm(initial={'variant_name':'variant'+str(variantcount+1)}),
#             'detail_form': ProductDetailForm,
#             'attr_value_form': VarAttrValueForm,
#             'product': product
#         }
#         status = request.GET.get("status", None)
#         if status is not None:
#             if status=="success":
#                 context["message"] = "Variant added !"
#         return render(request, "add_variant.html", context)

#     def post(self, request, id):
#         new_productvariant = ProductVariant(product_ref_id = id, variant_name =  request.POST.get("variant_name", None) )
#         new_productvariant.save()
#         new_productdetail = ProductDetail(product_ref_id = id, variant_ref_id = new_productvariant.variant_id, product_code=request.POST.get("product_code", None), product_image=request.FILES.get("product_image", None), selling_price=request.POST.get("selling_price", None))
#         new_productdetail.save()
        
#         attribute_refs = request.POST.getlist("attribute_ref")
#         values = request.POST.getlist("value")
#         for i in range(len(attribute_refs)):
#             new_attrvalue = VariantAttributeValue(variant_ref_id = new_productvariant.variant_id, attribute_ref_id = attribute_refs[i], value = values[i])
#             new_attrvalue.save()
#         return redirect("/products/"+ str(id)+ "/variant/add?status=success")

# class EditProduct(View):
#     def get(self, request, id):
#         context = {
#             'product_form': ProductForm(instance=Product.objects.get(product_id=id)),
#             'detail_form': ProductDetailForm2(instance=ProductDetail.objects.filter(product_ref=id, variant_ref=None).first())
#         }
#         status = request.GET.get("status", None)
#         if status is not None:
#             if status=="success":
#                 context["message"] = "Detail saved !"
#         return render(request, 'edit_product.html', context)
    
#     def post(self, request, id):
#         product_form_data = ProductForm(request.POST, instance=Product.objects.get(product_id=id))
#         if product_form_data.is_valid():
#             product = product_form_data.save()
#             if not product.has_variants:
                
#                 #if the product before has variants and now changed to 'has no variants', then variant details are deleted
#                 variants = ProductVariant.objects.filter(product_ref=id)
#                 if variants.count() > 0:
#                     var_attr_values = VariantAttributeValue.objects.filter(variant_ref__in=variants)
#                     var_attr_values.delete()
#                     product_details = ProductDetail.objects.filter(variant_ref__in=variants)
#                     for detail in product_details:
#                         if detail.product_image:
#                             if os.path.exists(detail.product_image.path):
#                                 os.remove(detail.product_image.path)
#                     product_details.delete()
#                     variants.delete()
                
#                 product_detail = ProductDetail.objects.filter(product_ref=id).first()
                
#                 #if the product before has image in product detail and now it is removed in form, then the existing file is deleted
#                 if request.POST.get("product_image-clear", None):
#                     if os.path.exists(product_detail.product_image.path):
#                         os.remove(product_detail.product_image.path)

#                 # below code saves product detail newly or updating existing
#                 detail_form_data = ProductDetailForm2(request.POST, request.FILES, instance=product_detail)
#                 detail = detail_form_data.save(commit=False)
#                 detail.product_ref = product
#                 detail.save()
#                 return redirect('/products/edit/'+str(id)+'?status=success')
#             else:

#                 #below code delete product detail if the product before has no variant now changed to have variants
#                 product_detail = ProductDetail.objects.filter(product_ref=id, variant_ref=None).first()
#                 if product_detail:
#                     if product_detail.product_image:
#                         if os.path.exists(product_detail.product_image.path):
#                             os.remove(product_detail.product_image.path)
#                     product_detail.delete()
#                     return redirect('add_variant', product.product_id)
                
#                 #just redirects to same page, if the product before has variants doesn't changed
#                 return redirect('/products/edit/'+str(id)+'?status=success')

# class EditVariant(View):
#     VarAttrValueFormset = inlineformset_factory(ProductVariant, VariantAttributeValue, form=VarAttrValueForm, extra=1)
#     def get(self, request, id):
#         variant = ProductVariant.objects.get(variant_id=id)
#         context = {
#             'variant': variant,
#             'variant_form': VariantForm(instance=variant),
#             'detail_form': ProductDetailForm2(instance=ProductDetail.objects.filter(variant_ref=id).first()),
#             'attr_value_formset': self.VarAttrValueFormset(queryset=VariantAttributeValue.objects.filter(variant_ref=id), instance=variant),
#             'attr_value_form': VarAttrValueForm
#         }
#         status = request.GET.get("status", None)
#         if status is not None:
#             if status=="success":
#                 context["message"] = "Variant edit saved !"
#         return render(request, "edit_variant.html", context)

#     def post(self, request, id):
#         variant = ProductVariant.objects.get(variant_id=id)

#         variant_form_data = VariantForm(request.POST, instance=variant )

#         product_detail = ProductDetail.objects.filter(variant_ref=id).first()
#         #if the variant before has image in product detail and now it is removed in form, then the existing file is deleted
#         if request.POST.get("product_image-clear", None):
#             if os.path.exists(product_detail.product_image.path):
#                 os.remove(product_detail.product_image.path)

#         product_detail_form_data = ProductDetailForm2(request.POST, request.FILES, instance=product_detail)
#         attr_values_formset_data = self.VarAttrValueFormset(request.POST, instance=variant)

#         if variant_form_data.is_valid() and product_detail_form_data.is_valid() and attr_values_formset_data.is_valid():
#             variant_form_data.save()
#             product_detail_form_data.save()
#             attr_values_formset_data.save()
#         return redirect("/products/variant/edit/"+str(id)+"?status=success")

# class DeleteProduct(View):
#     def get(self, request, id):
#         product = Product.objects.get(product_id = id)
#         product_detail = ProductDetail.objects.get(product_ref=id)
#         if product_detail.product_image:
#             if os.path.exists(product_detail.product_image.path):
#                 os.remove(product_detail.product_image.path)
#         product.delete()
#         return redirect('view_products')
    
# class DeleteVariant(View):
#     def get(self, request, id):
#         variant = ProductVariant.objects.get(variant_id = id)
#         product_detail = ProductDetail.objects.get(variant_ref=id)
#         if product_detail.product_image:
#             if os.path.exists(product_detail.product_image.path):
#                 os.remove(product_detail.product_image.path)
#         variant.delete()
#         return redirect('view_products')