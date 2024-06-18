from django import forms
from .models import *
   
class RequiredModelForm(forms.ModelForm):
    required_css_class = 'required'

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

# class ProductForm(RequiredModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'

# class ProductDetailForm(RequiredModelForm):
#     class Meta:
#         model = ProductDetail
#         fields = ['product_code', 'product_image',  'low_stock_threshold']

# class ProductDetailForm2(RequiredModelForm):
#     class Meta:
#         model = ProductDetail
#         fields = ['product_code', 'product_image', 'low_stock_threshold', 'is_active']

# class VariantForm(RequiredModelForm):
#     use_required_attribute = True
#     class Meta:
#         model = ProductVariant
#         fields = ['variant_name']

# class VarAttrValueForm(RequiredModelForm):
#     class Meta:
#         model = VariantAttributeValue
#         fields = ['product_attr_ref', 'value']

class SupplierForm(RequiredModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

# class PurchaseHeaderForm(RequiredModelForm):
#     class Meta:
#         model = PurchaseHeaderDetail
#         fields = ['supplier_ref']

# class PurchaseItemForm(RequiredModelForm):
#     class Meta:
#         model = PurchaseItem
#         fields = ['product_detail_ref', 'quantity', 'unit_cost_price']

class CustomerForm(RequiredModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = { 
            "dob" : forms.TextInput(attrs={"placeholder":"dd/mm/yyyy"})
        }

# class SaleHeaderForm(RequiredModelForm):
#     class Meta:
#         model = SaleHeaderDetail
#         fields = ['customer_ref','discount_percent', 'discount_amount']

# class SaleItemForm(RequiredModelForm):
#     class Meta:
#         model = SaleItem
#         fields = ['product_detail_ref','quantity','unit_sell_price']

class WarehouseForm(RequiredModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'

# class StockDetailForm(RequiredModelForm):
#     class Meta:
#         model = StockDetail
#         fields = ['warehouse_ref','product_detail_ref','quantity']
#         labels = {
#             'warehouse_ref': 'Choose Warehouse',
#             'product_detail_ref': 'Choose Product',
#             'quantity': 'Add or Minus Quantity'
#         }

# class ProductSelectForm(RequiredModelForm):
#     class Meta:
#         model = StockDetail
#         fields = ["product_detail_ref"]
#         labels = {
#             'product_detail_ref':'Choose Product'
#         }

# class TransferStockForm(RequiredModelForm):
#     class Meta:
#         model = StockDetail
#         fields = ["warehouse_ref", "quantity"]
#         labels = {
#             'warehouse_ref': "To warehouse",
#         }
#         widgets = {
#             "quantity": forms.NumberInput(attrs={"min":"0"})
#         }