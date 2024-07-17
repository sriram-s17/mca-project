from django.shortcuts import render, redirect
from database.models import *
from user.views import GroupRequiredMixin
from django.views import View
from django.utils import timezone
import calendar

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Create your views here.
class HomeView(GroupRequiredMixin, View):
    def get(self, request):
        context = {
            "low_stock_products": get_low_stock_products(),
            "last_month_sales": get_last_month_sales(),
            # "last_month_sales": get_last_month_sales(),
            "total_products": ProductDetail.objects.count(),
            "total_suppliers": Supplier.objects.count(),
            "total_customers": Customer.objects.count(),
        }
        return render(request, 'home.html', context)
    
def get_low_stock_products():
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

    return low_stock_products

def get_last_month_sales():
    today_date = timezone.now()
    month_year = str(today_date.year)+"-"+str(today_date.month-1)
    month, year = [today_date.month-1, today_date.year]
    from_dt = timezone.datetime(year, month, 1, 0, 0, tzinfo=timezone.get_current_timezone())
    
    to_dt = timezone.datetime(year, month, calendar.monthrange(year, month)[1], 0, 0, tzinfo=timezone.get_current_timezone())
    period = months[month-1] + " " + str(year)
    sales = SaleHeaderDetail.objects.filter(sold_date__range=(from_dt, to_dt))
    context = {
        "month_year": month_year,
        "period": period,
        "total_sales": sales.count()
    }
    return context    #new line added
    # total_sold_amount = 0
    # total_profit_amount = 0
    
    # for sale in sales:
    #     sale_items = SaleItem.objects.filter(sale_ref=sale)
        
    #     for item in sale_items:
    #         product_amount = item.quantity * item.unit_sell_price
    #         profit = product_amount - item.quantity * item.product_with_price_ref.cost_price

    #         total_sold_amount += product_amount
    #         total_profit_amount += profit

    # context = {
    #     "total_sold_amount": total_sold_amount,
    #     "total_profit_amount": total_profit_amount,
    #     "period": period,
    #     "month_year": month_year
    # }
    # return context