from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    class Meta:
        db_table = 'category'
    def __str__(self):
        return self.category_name

class Brand(models.Model):
    brand_id = models.BigAutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)
    class Meta:
        db_table = 'brand'
    def __str__(self):
        return self.brand_name

class Attribute(models.Model):
    attribute_id = models.BigAutoField(primary_key=True)
    attribute_name = models.CharField(max_length=60)
    class Meta:
        db_table = 'attribute'
    def __str__(self):
        return self.attribute_name

class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category_ref = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    brand_ref = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    has_variants = models.BooleanField(default=False)
    class Meta:
        db_table = 'product'
    def __str__(self):
        return str(self.product_name)

class ProductAttribute(models.Model):
    product_attr_id = models.BigAutoField(primary_key=True)
    product_ref = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute_ref = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    class Meta:
        db_table = 'product_attribute'
    def __str__(self):
        return str(self.attribute_ref)

class ProductVariant(models.Model):
    variant_id = models.BigAutoField(primary_key=True)
    product_ref = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant_name = models.CharField(max_length=100)
    class Meta:
        db_table = 'product_variant'
    def __str__(self):
        return str(self.variant_name)
    
class VariantAttributeValue(models.Model):
    variant_attr_value_id = models.BigAutoField(primary_key=True)
    variant_ref = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    product_attr_ref = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=60)
    class Meta:
        db_table = 'variant_attribute_value'
    def __str__(self):
        return str(self.variant_ref) + " " + str(self.value)

class ProductDetail(models.Model):
    product_detail_id = models.BigAutoField(primary_key=True)
    product_ref = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant_ref = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True, blank=True, default=None)
    product_code = models.CharField(max_length=30, unique=True, null=True, blank=True)
    product_image = models.ImageField(upload_to="product_images", null=True, blank=True, default=None)
    low_stock_threshold = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table = 'product_detail'
        ordering = ['product_ref']
    def __str__(self):
        if self.variant_ref:
            return self.product_code + " "+ str(self.variant_ref)
        else:
            return self.product_code + " "+ str(self.product_ref)

class ProductPrice(models.Model):
    product_price_id = models.BigAutoField(primary_key=True)
    product_detail_ref = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    cost_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    selling_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "product_price"
        ordering = ['product_detail_ref']
    def __str__(self):
        return str(self.product_detail_ref) + " cost:" + str(self.cost_price)

def get_default_user():
    return User.objects.get(id=1).pk
    #shopowner password: owner123
    
class Warehouse(models.Model):
    warehouse_id = models.BigAutoField(primary_key=True)
    warehouse_name = models.CharField(max_length=60)
    location = models.TextField(max_length=200, null=True, blank=True)
    incharge_person = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=get_default_user)
    class Meta:
        db_table = 'warehouse'
    def __str__(self):
        return self.warehouse_name

def get_warehouse_default():
    return Warehouse.objects.get(warehouse_id=1).pk

class StockDetail(models.Model):
    stock_id = models.BigAutoField(primary_key=True)
    warehouse_ref = models.ForeignKey(Warehouse, on_delete=models.SET_DEFAULT, default=get_warehouse_default)
    product_with_price_ref = models.ForeignKey(ProductPrice, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=(("good", "Good"), ("missed", "Missed"), ("damaged","Damaged")), default="good")
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "stock_detail"
    def __str__(self):
        return str(self.product_with_price_ref) + " " + str(self.quantity)

class Supplier(models.Model):
    supplier_id = models.BigAutoField(primary_key=True)
    shop_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=60)
    phone_regex = RegexValidator(regex=r'^(\d{10})$', message="Phone number must be entered in the 10 digit format: '9999999999'")
    phoneno = models.CharField(validators=[phone_regex], max_length=13, null=True, blank=True)
    address = models.TextField(max_length=200, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'supplier'
    def __str__(self):
        return self.shop_name

class PurchaseHeaderDetail(models.Model):
    purchase_id = models.BigAutoField(primary_key=True)
    supplier_ref = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    purchased_date = models.DateTimeField(auto_now_add=True)
    bill_amount = models.DecimalField(decimal_places=2, max_digits=10)
    class Meta:
        db_table = 'purchase_header_detail'
    def __str__(self):
        return str(self.purchased_date) + " " + str(self.supplier_ref)

class PurchaseItem(models.Model):
    purchase_item_id = models.BigAutoField(primary_key=True)
    purchase_ref = models.ForeignKey(PurchaseHeaderDetail, on_delete = models.CASCADE)
    product_detail_ref = models.ForeignKey(ProductDetail, on_delete = models.SET_NULL, null=True)
    quantity = models.IntegerField()
    unit_cost_price = models.DecimalField(decimal_places=2, max_digits=10)
    class Meta:
        db_table = 'purchase_item'
    def __str__(self):
        return self.product_detail_ref
    
class PurchasePayment(models.Model):
    purchase_payment_id = models.BigAutoField(primary_key=True)
    purchase_ref = models.ForeignKey(PurchaseHeaderDetail, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(decimal_places=2, max_digits=10)
    balance_amount = models.DecimalField(decimal_places=2, max_digits=10)
    class Meta:
        db_table = 'purchase_payment'
    def __str__(self):
        return str(self.payment_date)

class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    customer_name = models.CharField(max_length=60)
    gender = models.CharField(choices = (("male","Male"),("female","Female"), ("transgender","Transgender")), max_length=20, null=True, blank=True)
    dob_regex = RegexValidator(regex=r'^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$', message="dob must be in the format: dd/mm/yyyy")
    dob = models.CharField(validators=[dob_regex], max_length=20, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^(\d{10})$', message="Phone number must be entered in the 10 digit format: '9999999999'")
    phoneno = models.CharField(validators=[phone_regex], max_length=13, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(max_length=100, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "customer"
    def __str__(self):
        return self.customer_name

class SaleHeaderDetail(models.Model):
    sale_id = models.BigAutoField(primary_key=True)
    customer_ref = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    sold_date = models.DateTimeField(auto_now_add=True)
    bill_amount = models.DecimalField(decimal_places=2, max_digits=10)
    discount_percent = models.DecimalField(default=0, blank=True, decimal_places=2, max_digits=10)
    discount_amount = models.DecimalField(default=0, blank=True, decimal_places=2, max_digits=10)
    class Meta:
        db_table = 'sale_header_detail'
    def __str__(self):
        return str(self.sold_date) + " " + str(self.customer_ref)

class SaleItem(models.Model):
    sale_item_id = models.BigAutoField(primary_key=True)
    sale_ref = models.ForeignKey(SaleHeaderDetail, on_delete = models.CASCADE)
    product_with_price_ref = models.ForeignKey(ProductPrice, on_delete = models.SET_NULL, null=True)
    quantity = models.IntegerField()
    unit_sell_price = models.DecimalField(decimal_places=2, max_digits=10)
    class Meta:
        db_table = 'sale_item'
    def __str__(self):
        return self.product_detail_ref

class SalePayment(models.Model):
    sale_payment_id = models.BigAutoField(primary_key=True)
    sale_ref = models.ForeignKey(SaleHeaderDetail, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(decimal_places=2, max_digits=10)
    balance_amount = models.DecimalField(decimal_places=2, max_digits=10)
    class Meta:
        db_table = 'sale_payment'
    def __str__(self):
        return str(self.payment_date)