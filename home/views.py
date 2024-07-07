from django.shortcuts import render, redirect
from database.models import *
from user.views import GroupRequiredMixin
from django.views import View

# Create your views here.
class HomeView(GroupRequiredMixin, View):
    groups_required =  ['owner']
    def get(self, request):
        ppid_pdid = {product[0]:product[1] for product in ProductPrice.objects.all().values_list("product_price_id", "product_detail_ref_id")}
        pdid_thresholds = {product[0]:product[1] for product in ProductDetail.objects.all().values_list("product_detail_id", "low_stock_threshold")}
        stock_details = StockDetail.objects.filter(status="good")
        low_stock_products= {}
        all_products = {}
        for stock in stock_details:
            if stock.product_with_price_ref not in all_products:
                all_products.update({stock.product_with_price_ref : {"quantity": stock.quantity, "low_stock_threshold":pdid_thresholds[ppid_pdid[stock.product_with_price_ref_id]]}})
            else:
                all_products[stock.product_with_price_ref]["quantity"] += stock.quantity

        for product_price_ref, stock_detail in all_products.items():
            if stock_detail["quantity"] <= stock_detail["low_stock_threshold"]:
                low_stock_products.update({product_price_ref.product_detail_ref: stock_detail})
        context = {
            "low_stock_products": low_stock_products
        }
        return render(request, 'home.html', context)