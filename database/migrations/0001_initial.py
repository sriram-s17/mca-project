# Generated by Django 5.0.6 on 2024-05-27 09:52

import database.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('brand_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=60)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phoneno', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the 10 digit format: '9999999999'", regex='^(\\d{10})$')])),
                ('address', models.TextField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('prod_detail_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_code', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('selling_price', models.IntegerField(blank=True, null=True)),
                ('low_stock_threshold', models.IntegerField(default=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'product_details',
            },
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('purchase_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('purchased_date', models.DateTimeField(auto_now_add=True)),
                ('bill_amount', models.IntegerField()),
                ('total_amount', models.IntegerField()),
            ],
            options={
                'db_table': 'purchases',
            },
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('supplier_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('shop_name', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=60)),
                ('phoneno', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the 10 digit format: '9999999999'", regex='^(\\d{10})$')])),
                ('address', models.TextField(blank=True, max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'suppliers',
            },
        ),
        migrations.CreateModel(
            name='VariantAttributes',
            fields=[
                ('attribute_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('attribute_name', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'product_attributes',
            },
        ),
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('price_history_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cost_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('product_detail_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.productdetails')),
            ],
            options={
                'db_table': 'price_history',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('has_variants', models.BooleanField(default=False)),
                ('brand_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.brands')),
                ('category_ref', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.categories')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.AddField(
            model_name='productdetails',
            name='product_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.products'),
        ),
        migrations.CreateModel(
            name='ProductVariants',
            fields=[
                ('variant_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('variant_name', models.CharField(max_length=100, null=True)),
                ('product_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.products')),
            ],
            options={
                'db_table': 'product_variants',
            },
        ),
        migrations.AddField(
            model_name='productdetails',
            name='variant_ref',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.productvariants'),
        ),
        migrations.CreateModel(
            name='PurchasePayments',
            fields=[
                ('purchase_payment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('paid_amount', models.IntegerField()),
                ('balance_amount', models.IntegerField()),
                ('purchase_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.purchases')),
            ],
            options={
                'db_table': 'purchase_payments',
            },
        ),
        migrations.CreateModel(
            name='PurchaseDetails',
            fields=[
                ('purchase_detail_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('unit_cost_price', models.IntegerField()),
                ('product_detail_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.productdetails')),
                ('purchase_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.purchases')),
            ],
            options={
                'db_table': 'purchase_details',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('sale_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('sold_date', models.DateTimeField(auto_now_add=True)),
                ('bill_amount', models.IntegerField()),
                ('discount_percent', models.IntegerField(default=0)),
                ('discount_amount', models.IntegerField(default=0)),
                ('total_amount', models.IntegerField()),
                ('customer_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.customers')),
            ],
            options={
                'db_table': 'sales',
            },
        ),
        migrations.CreateModel(
            name='SalePayments',
            fields=[
                ('sale_payment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('paid_amount', models.IntegerField()),
                ('balance_amount', models.IntegerField()),
                ('sale_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.sales')),
            ],
            options={
                'db_table': 'sale_payments',
            },
        ),
        migrations.CreateModel(
            name='SaleDetails',
            fields=[
                ('sale_detail_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('unit_sell_price', models.IntegerField()),
                ('product_detail_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.productdetails')),
                ('sale_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.sales')),
            ],
            options={
                'db_table': 'sale_details',
            },
        ),
        migrations.AddField(
            model_name='purchases',
            name='supplier_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.suppliers'),
        ),
        migrations.CreateModel(
            name='VariantAttributeValues',
            fields=[
                ('variant_attr_value_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=60)),
                ('attribute_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.variantattributes')),
                ('variant_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.productvariants')),
            ],
            options={
                'db_table': 'prod_attr_values',
            },
        ),
        migrations.CreateModel(
            name='Warehouses',
            fields=[
                ('warehouse_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('warehouse_name', models.CharField(max_length=60)),
                ('location', models.TextField(blank=True, max_length=200, null=True)),
                ('incharge_person', models.ForeignKey(default=database.models.get_default_user, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'warehouses',
            },
        ),
        migrations.CreateModel(
            name='StockDetails',
            fields=[
                ('stock_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('product_detail_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.productdetails')),
                ('warehouse_ref', models.ForeignKey(default=database.models.get_warehouse_default, on_delete=django.db.models.deletion.SET_DEFAULT, to='database.warehouses')),
            ],
            options={
                'db_table': 'stock_details',
            },
        ),
    ]
