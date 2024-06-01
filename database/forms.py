from django.forms import ModelForm
from .models import *
   
class RequiredModelForm(ModelForm):
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

class ProductForm(RequiredModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductDetailForm(RequiredModelForm):
    class Meta:
        model = ProductDetail
        fields = ['product_code', 'product_image', 'selling_price', 'low_stock_threshold']

class ProductDetailForm2(RequiredModelForm):
    class Meta:
        model = ProductDetail
        fields = ['product_code', 'product_image', 'selling_price', 'low_stock_threshold', 'is_active']

class VariantForm(RequiredModelForm):
    use_required_attribute = True
    class Meta:
        model = ProductVariant
        fields = ['variant_name']

class VarAttrValueForm(RequiredModelForm):
    class Meta:
        model = VariantAttributeValue
        fields = ['attribute_ref', 'value']

class SupplierForm(RequiredModelForm):
    class Meta:
        model = Supplier
        fields = ['shop_name', 'owner_name', 'phoneno', 'address']

# class SupplierRefForm(RequiredModelForm):
#     class Meta:
#         model = Purchases
#         fields = ['supplier_ref']

# class PurchaseDetailForm(RequiredModelForm):
#     class Meta:
#         model = PurchaseDetails
#         fields = ['product_detail_ref', 'unit_cost_price', 'quantity']

class CustomerForm(RequiredModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

# class CustomerRefForm(RequiredModelForm):
#     class Meta:
#         model = Sales
#         fields = ['customer_ref']

# class SaleDetailsForm(RequiredModelForm):
#     class Meta:
#         model = SaleDetails
#         fields = ['product_detail_ref','quantity','unit_sell_price']


class WarehouseForm(RequiredModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'

# # class imageuploadform(RequiredModelForm):
# #     class Meta:
# #         model = testimageupload
# #         fields = '__all__'