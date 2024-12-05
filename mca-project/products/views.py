from django.shortcuts import render, redirect
from django.views import View
from database.forms import *
import os
from json import dumps
from django.forms import inlineformset_factory, modelformset_factory
from user.views import GroupRequiredMixin
import pprint
from django.db import connection
# Create your views here.

#products views
class ViewProducts(GroupRequiredMixin, View):
    groups_required = ['Owner', 'Salesman']
    def get(self, request):
        products = Product.objects.all()
        # After executing a query
        # print(products.db)
        # print(connection.alias)
        context = {
            "products":get_product_details(products)
        }
        return render(request, 'products.html', context)
    
def get_product_details(products):
    product_list = []
    for product in products:
        product_list.append({"product_ref":product})
    
    for product in product_list:
        if product["product_ref"].has_variants == True:
            variants = ProductVariant.objects.filter(product_ref=product["product_ref"])
            variant_list = []
            for variant in variants:
                product_detail = ProductDetail.objects.get(variant_ref=variant)
                var_attr_values = VariantAttributeValue.objects.filter(variant_ref=variant)
                attributes = {}
                for var_attr_value in var_attr_values:
                    attributes.update({var_attr_value.product_attr_ref.attribute_ref.attribute_name : var_attr_value.value})
                
                variant = {"variant_ref":variant, "product_detail_ref":product_detail, "attributes": attributes }
                variant_list.append(variant)
            product.update({"variants":variant_list})
        else:
            product_detail = ProductDetail.objects.get(product_ref = product["product_ref"])
            product.update({"product_detail_ref": product_detail})
    return product_list

# class ViewProducts(View):
#     def get(self, request):
#         products = ProductDetail.objects.all().order_by("variant_ref")
#         product_list = []
#         for product in products:
#             product_list.append({"product_id":product.product_ref.product_id,
#                                  "product_detail_id":product.product_detail_id,
#                                  "product_name":product.product_ref.product_name,
#                                  "category":product.product_ref.category_ref,
#                                  "brand":product.product_ref.brand_ref,
#                                  "variants": get_variant_detail(product.variant_ref) if product.variant_ref else product.variant_ref,
#                                  "product_code":product.product_code,
#                                  "is_active":product.is_active,
#             })
            
#         context = {
#             "products" : product_list
#         }
#         return render(request, 'products.html', context)
    
# def get_variant_detail(variant_ref):
#     VarAttrValues = VariantAttributeValue.objects.filter(variant_ref=variant_ref)
#     variant = {"name": variant_ref.variant_name}
#     if VarAttrValues:
#         attributes = {"attributes":{}}
#         for attr_value in VarAttrValues:
#             attributes["attributes"].update({attr_value.product_attr_ref.attribute_ref: attr_value.value})
#         variant.update(attributes)
#     return variant

class ViewProduct(GroupRequiredMixin, View):
    groups_required = ['Owner', 'Salesman']
    def get(self, request, id):
        product = Product.objects.get(product_id=id)
        product_dict = {"product_id":product.product_id, "product_name": product.product_name,
                        "category_ref": product.category_ref, "brand_ref": product.brand_ref,
                        "description":product.description, "has_variants":product.has_variants}
        
        if product_dict["has_variants"]:
            variants = ProductVariant.objects.filter(product_ref=product_dict["product_id"])
            variants_list = []
            if variants:
                for variant in variants:
                    variant_dict = {"variant_id": variant.variant_id, "variant_name":variant.variant_name}
                    
                    var_attr_values = VariantAttributeValue.objects.filter(variant_ref=variant)
                    attr_values_list = []
                    for attr_value in var_attr_values:
                        attr_values_list.append({"attribute":attr_value, "value":attr_value.value})
                    variant_dict.update({"attr_values":attr_values_list})
                    
                    product_detail = ProductDetail.objects.filter(variant_ref=variant)[0]
                    variant_dict.update({"product_detail_id":product_detail.product_detail_id, "product_code":product_detail.product_code, 
                                 "product_image":product_detail.product_image, "selling_price":product_detail.selling_price, 
                                 "low_stock_threshold": product_detail.low_stock_threshold, "is_active":product_detail.is_active})

                    stock = StockDetail.objects.filter(product_detail_ref = product_detail)
                    if stock:
                        stock = stock[0]
                        variant_dict.update({"quantity": stock.quantity})
                    
                    variants_list.append(variant_dict)
                product_dict.update({"variants":variants_list})
        else:
            product_detail = ProductDetail.objects.filter(product_ref=product_dict["product_id"])[0]
            product_dict.update({"product_detail_id":product_detail.product_detail_id, "product_code":product_detail.product_code, 
                                 "product_image":product_detail.product_image, "selling_price":product_detail.selling_price, 
                                 "low_stock_threshold": product_detail.low_stock_threshold, "is_active":product_detail.is_active})
            
            stock = StockDetail.objects.filter(product_detail_ref = product_detail)[0]
            if stock:
                product_dict.update({"quantity": stock.quantity})
        
        return render(request, "view_product.html", {"product":product_dict})

class AddProduct(GroupRequiredMixin, View):
    def get(self, request):
        context = {'product_form': ProductForm, 'detail_form': ProductDetailForm, 'attribute_form':ProductAttributeForm, 'selling_price_form': SellingPriceForm}
        status = request.GET.get("status")
        if status:
            if status == 'success':
                context["message"] = "product added!"
        return render(request, 'add_product.html', context )
    
    def post(self, request):
        product_form_data = ProductForm(request.POST)
        if product_form_data.is_valid():
            if request.POST.get("has_variants", None):
                product = product_form_data.save()
                attribute_ref_ids = request.POST.getlist("attribute_ref")
                for attr_id in attribute_ref_ids:
                    new_product_attribute = ProductAttribute(product_ref_id=product.product_id, attribute_ref_id = attr_id)
                    new_product_attribute.save()
                return redirect('add_variant', product.product_id)
            else:
                detail_form_data = ProductDetailForm(request.POST, request.FILES)
                if detail_form_data.is_valid():
                    product = product_form_data.save()
                    detail = detail_form_data.save(commit=False)
                    detail.product_ref = product
                    detail.save()
                    selling_price = request.POST.get("selling_price", None)
                    if selling_price:
                        new_price = ProductPrice(product_detail_ref_id=detail.product_detail_id ,selling_price=selling_price)
                        new_price.save()
                    return redirect('/products/add?status=success')
                else:
                    context = {'product_form': product_form_data, 'detail_form': detail_form_data, 'attribute_form':ProductAttributeForm}
                    return render(request, 'add_product.html', context)

class EditProduct(GroupRequiredMixin, View):
    attribute_formset = modelformset_factory(ProductAttribute, form=ProductAttributeForm, extra=0, can_delete=True)
    price_formset = modelformset_factory(ProductPrice, form=SellingPriceForm2, extra=0)
    def get(self, request, id):
        product = Product.objects.get(product_id=id)
        product_detail = ProductDetail.objects.filter(product_ref=id, variant_ref=None).first()
        
        context = {
            'product_form': ProductForm(instance=product),
            'detail_form': ProductDetailForm2(instance=product_detail),
            'attribute_form': ProductAttributeForm,
        }
        if product.has_variants:
            product_attributes = ProductAttribute.objects.filter(product_ref=product)
            if product_attributes:
                context.update({
                    'attribute_formset': self.attribute_formset(queryset=product_attributes),
                    'selling_price_form': SellingPriceForm
                })
        else:
            product_prices = ProductPrice.objects.filter(product_detail_ref=product_detail)
            if product_prices.count() ==  1:
                context['selling_price_form'] = SellingPriceForm(instance=product_prices.first())
            else:
                nonzerostockproductsprices = StockDetail.objects.filter(product_with_price_ref__in=product_prices, quantity__gt=0).values_list("product_with_price_ref")
                if nonzerostockproductsprices:
                    context['price_formset'] = self.price_formset(queryset=product_prices.filter(product_price_id__in = nonzerostockproductsprices))            

        status = request.GET.get("status", None)
        if status is not None:
            if status=="success":
                context["message"] = "Product Detail saved !"
            elif status == 'error':
                context["error"] = "Something gone error!"
        return render(request, 'edit_product.html', context)
    
    def post(self, request, id):
        product_form_data = ProductForm(request.POST, instance=Product.objects.get(product_id=id))
        if product_form_data.is_valid():
            product = product_form_data.save()
            if product.has_variants:                
                #this below is for product already has variants doesn't changed and also for changed 
                #saves new attributes 
                attribute_ref_ids = request.POST.getlist("attribute_ref")
                for attr_id in attribute_ref_ids:
                    new_product_attribute = ProductAttribute(product_ref_id=product.product_id, attribute_ref_id = attr_id)
                    new_product_attribute.save()

                #saves modified attributes
                attr_formset_values = self.attribute_formset(request.POST)
                if attr_formset_values:
                    if attr_formset_values.is_valid():
                        attr_formset_values.save()

                #this portion is for change of product has no variants to have variants
                #below code delete product detail if the product before has no variant now changed to have variants
                product_detail = ProductDetail.objects.filter(product_ref=product, variant_ref=None).first()
                if product_detail:
                    if product_detail.product_image:
                        if os.path.exists(product_detail.product_image.path):
                            os.remove(product_detail.product_image.path)
                    product_detail.delete()
                    return redirect('add_variant', product.product_id)

                #just redirects to same page, if the product before has variants doesn't changed
                return redirect('/products/edit/'+str(id)+'?status=success')
            else:
                #if the product before has variants and now changed to 'has no variants', then variant details are deleted
                variants = ProductVariant.objects.filter(product_ref=id)
                if variants.count() > 0:
                    product_details = ProductDetail.objects.filter(variant_ref__in=variants)
                    for detail in product_details:
                        if detail.product_image:
                            if os.path.exists(detail.product_image.path):
                                os.remove(detail.product_image.path)
                    product_details.delete()
                    variants.delete()
                product_attributes = ProductAttribute.objects.filter(product_ref=id)
                product_attributes.delete()
                
                #it is for getting product detail if the product before also has no variants
                product_detail = ProductDetail.objects.filter(product_ref=id).first()
                
                #if the product before has image in product detail and now it is removed in form, then the existing file is deleted
                if request.POST.get("product_image-clear", None) or request.FILES.get("product_image", None):
                    if product_detail.product_image:
                        if os.path.exists(product_detail.product_image.path):
                            os.remove(product_detail.product_image.path)

                # below code saves product detail newly or updating existing
                detail_form_data = ProductDetailForm2(request.POST, request.FILES, instance=product_detail)
                if detail_form_data.is_valid():
                    detail = detail_form_data.save(commit=False)
                    detail.product_ref = product
                    detail.save()
                    product_prices = ProductPrice.objects.filter(product_detail_ref=detail)
                    selling_price = request.POST.get("selling_price", None)
                    if selling_price:
                        if product_prices.count() == 1:
                            product_price = product_prices.first()
                            if product_price.selling_price != float(selling_price):
                                product_price.selling_price = float(selling_price)
                                product_price.save()
                        elif product_prices.count() == 0:
                            new_price = ProductPrice(product_detail_ref_id=detail.product_detail_id ,selling_price=selling_price)
                            new_price.save()
                    else:
                        nonzerostockproductsprices = StockDetail.objects.filter(product_with_price_ref__in=product_prices, quantity__gt=0).values_list("product_with_price_ref")
                        price_formset_data = self.price_formset(request.POST, queryset=product_prices.filter(product_price_id__in = nonzerostockproductsprices))
                        price_formset_data.save()
                    return redirect('/products/edit/'+str(id)+'?status=success')
                else:
                    return redirect('/products/edit/'+str(id)+'?status=error')

class AddVariant(GroupRequiredMixin, View):
    def get(self, request, id):
        variantcount = ProductVariant.objects.filter(product_ref=id).count()
        product = Product.objects.get(product_id = id)
        attr_value_forms = []
        product_attributes = ProductAttribute.objects.filter(product_ref=product)
        if product_attributes:
            for attr in product_attributes:
                attr_value_forms.append(VarAttrValueForm(initial={"product_attr_ref":attr.product_attr_id}, 
                                                                     label_suffix=" "+str(attr.attribute_ref), 
                                                                     auto_id="id_%s_"+str(attr.product_attr_id)
                                                                     ))
        context = {
            'variant_form': VariantForm(initial={'variant_name':'variant'+str(variantcount+1)}),
            'detail_form': ProductDetailForm,
            'attr_value_forms':attr_value_forms,
            'selling_price_form':SellingPriceForm,
            'product': product
        }
        
        status = request.GET.get("status", None)
        if status is not None:
            if status=="success":
                context["message"] = "Variant added !"

        return render(request, "add_variant.html", context)

    def post(self, request, id):
        new_variant = ProductVariant(product_ref_id = id, variant_name =  request.POST.get("variant_name", None) )
        new_variant.save()
        new_productdetail = ProductDetail(product_ref_id = id, variant_ref_id = new_variant.variant_id, product_code=request.POST.get("product_code", None), product_image=request.FILES.get("product_image", None), low_stock_threshold = request.POST.get("low_stock_threshold", None))
        new_productdetail.save()
        
        selling_price = request.POST.get("selling_price", None)
        if selling_price:
            new_price = ProductPrice(product_detail_ref_id=new_productdetail.product_detail_id ,selling_price=selling_price)
            new_price.save()
        
        attribute_refs = request.POST.getlist("product_attr_ref")
        values = request.POST.getlist("value")
        for i in range(len(attribute_refs)):
            new_attrvalue = VariantAttributeValue(variant_ref_id = new_variant.variant_id, product_attr_ref_id = attribute_refs[i], value = values[i])
            new_attrvalue.save()
        return redirect("/products/"+ str(id)+ "/variant/add?status=success")

class EditVariant(GroupRequiredMixin, View):
    VarAttrValueFormset = modelformset_factory(VariantAttributeValue, form=VarAttrValueForm, extra=0)
    price_formset = modelformset_factory(ProductPrice, form=SellingPriceForm2, extra=0)
    def get(self, request, id):
        variant = ProductVariant.objects.get(variant_id=id)
        product_detail = ProductDetail.objects.filter(variant_ref=id).first()
        product_price = ProductPrice.objects.filter(product_detail_ref=product_detail).order_by('updated_date').last()
        var_attr_values = VariantAttributeValue.objects.filter(variant_ref=variant)
        context = {
            'variant': variant,
            'variant_form': VariantForm(instance=variant),
            'detail_form': ProductDetailForm2(instance=product_detail),
            'attr_value_formset': self.VarAttrValueFormset(queryset=var_attr_values),
        }

        no_value_attr_value_forms = []
        attributes = [instance.product_attr_ref.attribute_ref for instance in var_attr_values]
        no_value_attributes = ProductAttribute.objects.filter(product_ref=product_detail.product_ref).exclude(attribute_ref__in = attributes)
        if no_value_attributes:
            for attr in no_value_attributes:
                no_value_attr_value_forms.append(VarAttrValueForm(initial={"product_attr_ref":attr.product_attr_id}, 
                                                                     label_suffix=" "+str(attr.attribute_ref), 
                                                                     auto_id="id_%s_"+str(attr.product_attr_id)
                                                                     ))
        if no_value_attr_value_forms:
            context["no_value_attr_value_forms"] = no_value_attr_value_forms

        product_prices = ProductPrice.objects.filter(product_detail_ref=product_detail)
        if product_prices.count() ==  1:
            context['selling_price_form'] = SellingPriceForm(instance=product_prices.first())
        else:
            nonzerostockproductsprices = StockDetail.objects.filter(product_with_price_ref__in=product_prices, quantity__gt=0).values_list("product_with_price_ref")
            if nonzerostockproductsprices:
                context['price_formset'] = self.price_formset(queryset=product_prices.filter(product_price_id__in = nonzerostockproductsprices))            

        status = request.GET.get("status", None)
        if status is not None:
            if status=="success":
                context["message"] = "Variant Details saved !"
            elif status=="error":
                context["error"] = "Something Gone Error!"
        return render(request, "edit_variant.html", context)

    def post(self, request, id):
        variant = ProductVariant.objects.get(variant_id=id)
        variant_form_data = VariantForm(request.POST, instance=variant )

        product_detail = ProductDetail.objects.filter(variant_ref=variant).first()
        
        #if the variant before has image in product detail and now it is removed in form, then the existing file is deleted
        if request.POST.get("product_image-clear", None) or request.FILES.get("product_image", None):
            if product_detail.product_image:
                if os.path.exists(product_detail.product_image.path):
                    os.remove(product_detail.product_image.path)

        product_detail_form_data = ProductDetailForm2(request.POST, request.FILES, instance=product_detail)
        attr_values_formset_data = self.VarAttrValueFormset(request.POST)

        if variant_form_data.is_valid() and product_detail_form_data.is_valid():
            variant_form_data.save()
            product_detail_form_data.save()
            if attr_values_formset_data.is_valid():
                attr_values_formset_data.save()

            # if new attribute added in edited product, then value for the attribute is saved
            attribute_refs = request.POST.getlist("product_attr_ref")
            values = request.POST.getlist("value")
            if attribute_refs:
                for i in range(len(attribute_refs)):
                    new_attrvalue = VariantAttributeValue(variant_ref_id = variant.variant_id, product_attr_ref_id = attribute_refs[i], value = values[i])
                    new_attrvalue.save()

            product_prices = ProductPrice.objects.filter(product_detail_ref=product_detail)
            selling_price = request.POST.get("selling_price", None)
            if selling_price:
                if product_prices.count() == 1:
                    product_price = product_prices.first()
                    if product_price.selling_price != float(selling_price):
                        product_price.selling_price = float(selling_price)
                        product_price.save()
                elif product_prices.count() == 0:
                    new_price = ProductPrice(product_detail_ref_id=product_detail.product_detail_id ,selling_price=selling_price)
                    new_price.save()
            else:
                nonzerostockproductsprices = StockDetail.objects.filter(product_with_price_ref__in=product_prices, quantity__gt=0).values_list("product_with_price_ref")
                price_formset_data = self.price_formset(request.POST, queryset=product_prices.filter(product_price_id__in = nonzerostockproductsprices))
                price_formset_data.save()
        else:
            return redirect('/products/variant/edit/'+str(id)+'?status=error')

        return redirect("/products/variant/edit/"+str(id)+"?status=success")

class DeleteProduct(GroupRequiredMixin, View):
    def get(self, request, id):
        product = Product.objects.get(product_id = id)
        product_detail = ProductDetail.objects.get(product_ref=id)
        if product_detail.product_image:
            if os.path.exists(product_detail.product_image.path):
                os.remove(product_detail.product_image.path)
        product.delete()
        return redirect('view_products')
    
class DeleteVariant(GroupRequiredMixin, View):
    def get(self, request, id):
        variant = ProductVariant.objects.get(variant_id = id)
        product_detail = ProductDetail.objects.get(variant_ref=id)
        if product_detail.product_image:
            if os.path.exists(product_detail.product_image.path):
                os.remove(product_detail.product_image.path)
        variant.delete()
        return redirect('view_products')