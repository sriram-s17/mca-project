from typing import Any
from django import forms
from .models import *
   
class RequiredModelForm(forms.ModelForm):
    required_css_class = 'required'

class ChangePwdForm(forms.Form):
    required_css_class = "required"
    username = forms.CharField(widget=forms.TextInput())
    new_password = forms.CharField(widget=forms.PasswordInput())

class CategoryForm(RequiredModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BrandForm(RequiredModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

class AttributeForm(RequiredModelForm):
    class Meta:
        model = Attribute
        fields = '__all__'

class ProductForm(RequiredModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # widgets = {
        #     "has_variants":forms.CheckboxInput(attrs={"class":"form-check-input","role":"switch"})
        # }

class ProductDetailForm(RequiredModelForm):
    class Meta:
        model = ProductDetail
        fields = ['product_code', 'product_image',  'low_stock_threshold']

class ProductDetailForm2(RequiredModelForm):
    class Meta:
        model = ProductDetail
        fields = ['product_code', 'product_image', 'low_stock_threshold', 'is_active']

class SellingPriceForm(RequiredModelForm):
    class Meta:
        model = ProductPrice
        fields = ['selling_price']

class SellingPriceForm2(RequiredModelForm):
    class Meta:
        model = ProductPrice
        fields = ['selling_price']
        
    def __init__(self, *args, **kwargs):
        super(SellingPriceForm2, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            stockcount = StockDetail.objects.filter(product_with_price_ref=self.instance).first().quantity
            self.fields['selling_price'].label = f"Selling Price of Product having cost Rs.{self.instance.cost_price}"
            self.fields['selling_price'].help_text = f"Available stock in this price = {stockcount}"

# class PriceFormset(forms.BaseModelFormSet):
#      def __init__(self, *args, **kwargs):
#         super(PriceFormset, self).__init__(*args, **kwargs)
#         forms = []
#         for form in self.forms:
#             # Assuming you have an `is_deletable` field to determine if an item is deletable
#             stockcount = StockDetail.objects.filter(product_with_price_ref=form.instance).first().quantity
#             if stockcount>0:
#                 forms.append(form)
#         self.forms = forms
#     def __iter__(self):
        

class ProductAttributeForm(RequiredModelForm):
    class Meta:
        model = ProductAttribute
        fields = ['attribute_ref']
        labels = {
            "attribute_ref": "Attribute"
        }

class VariantForm(RequiredModelForm):
    use_required_attribute = True
    class Meta:
        model = ProductVariant
        fields = ['variant_name']

class VarAttrValueForm(RequiredModelForm):
    class Meta:
        model = VariantAttributeValue
        fields = ['product_attr_ref', 'value']
        #this label is used in add variant page
        labels = {
            "value":"Value of"
        }
        widgets = {
            "product_attr_ref":forms.HiddenInput()
        }

        #this label is used in edit variant page and the form is used as modelformset
    def __init__(self, *args, **kwargs):
        super(VarAttrValueForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['value'].label = f"value of {self.instance.product_attr_ref.attribute_ref}"

class SupplierForm(RequiredModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class PurchaseHeaderForm(RequiredModelForm):
    class Meta:
        model = PurchaseHeaderDetail
        fields = ['supplier_ref']

class PurchaseItemForm(RequiredModelForm):
    class Meta:
        model = PurchaseItem
        fields = ['product_detail_ref', 'quantity', 'unit_cost_price']
        labels = {
            'product_detail_ref': 'Product'
        }
        widgets = {
            "quantity": forms.NumberInput(attrs={"min":"0"})
        }
    def __init__(self, *args, **kwargs):
        super(PurchaseItemForm, self).__init__(*args, **kwargs)
        self.fields['product_detail_ref'].queryset = ProductDetail.objects.all().order_by("product_ref")

class CustomerForm(RequiredModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = { 
            "dob" : forms.TextInput(attrs={"placeholder":"dd/mm/yyyy"})
        }

class SaleHeaderForm(RequiredModelForm):
    class Meta:
        model = SaleHeaderDetail
        fields = ['customer_ref','discount_percent', 'discount_amount']

class SaleItemForm(RequiredModelForm):
    class Meta:
        model = SaleItem
        fields = ['product_with_price_ref','quantity','unit_sell_price']
        labels = {
            'product_with_price_ref': 'Product'
        }
        widgets = {
            "quantity": forms.NumberInput(attrs={"min":"0"})
        }
    def __init__(self, *args, **kwargs):
        super(SaleItemForm, self).__init__(*args, **kwargs)
        stocked_product_price_ids = StockDetail.objects.filter(quantity__gt=0).values_list("product_with_price_ref").distinct()
        product_price_ids = [id[0] for id in stocked_product_price_ids]
        self.fields['product_with_price_ref'].queryset = ProductPrice.objects.filter(product_price_id__in=list(product_price_ids)).order_by("product_detail_ref")

class WarehouseForm(RequiredModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'

class StockDetailForm(RequiredModelForm):
    class Meta:
        model = StockDetail
        fields = ['warehouse_ref','product_with_price_ref','quantity', "status"]
        labels = {
            'warehouse_ref': 'Choose Warehouse',
            'product_with_price_ref': 'Choose Product',
            "quantity":"Available Quantity",
            'status': 'Stock Condition'
        }
        widgets = {
            'quantity': forms.NumberInput(attrs={"min":"0", "readonly":"true"})
        }
    def __init__(self, *args, **kwargs):
        super(StockDetailForm, self).__init__(*args, **kwargs)
        # self.fields["product_with_price_ref"].queryset = ProductPrice.objects.all().order_by("product_detail_ref")

class ProductSelectForm(RequiredModelForm):
    class Meta:
        model = StockDetail
        fields = ["product_with_price_ref"]
        labels = {
            'product_with_price_ref':'Choose Product'
        }

class TransferStockForm(RequiredModelForm):
    class Meta:
        model = StockDetail
        fields = ["warehouse_ref", "quantity"]
        labels = {
            'warehouse_ref': "To warehouse",
        }
        help_texts = {
            "warehouse_ref": "Source and Destination should not be same"
        }
        widgets = {
            "quantity": forms.NumberInput(attrs={"min":"0"})
        }

class ProductDetailSelectForm(forms.Form):
    product_detail_ref = forms.ModelChoiceField(queryset=ProductDetail.objects.all(), label="Choose Product")

class CustomerSelectForm(forms.Form):
    customer_ref = forms.ModelChoiceField(queryset=Customer.objects.all(), label="Select Customer")