from django.shortcuts import render, redirect
from django.views import View
from database.models import *
from django.utils import timezone
import calendar
from user.views import GroupRequiredMixin

# Create your views here.
class ViewReport1(GroupRequiredMixin, View):
    def get(self, request):
        requested_period = request.GET.get("month_year", None)
        default_period = request.GET.get("default", "last 30 days")
        context = {}
        if requested_period:
            year, month = map(lambda x: int(x), requested_period.split("-"))

            from_dt = timezone.datetime(year, month, 1, 0, 0, tzinfo=timezone.get_current_timezone())
            
            to_dt = timezone.datetime(year, month, calendar.monthrange(year, month)[1], 0, 0, tzinfo=timezone.get_current_timezone())
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            period = months[month-1] + " " + str(year)
            sales = SaleHeaderDetail.objects.filter(sold_date__range=(from_dt, to_dt))
        elif default_period:
            if default_period == "last 30 days":
                period = default_period
                sales = SaleHeaderDetail.objects.filter(sold_date__gte=timezone.now()-timezone.timedelta(days=30))
        context = profit_of_sales(sales)
        context.update({"period":period})
        
        return render(request, "view_report1.html", context)
    
def profit_of_sales(sales):
    sold_amount = 0
    profit = 0
    most_sold_items = {}
    
    for sale in sales:
        # sold_amount += sale.bill_amount
        sale_items = SaleItem.objects.filter(sale_ref=sale)
        
        for item in sale_items:
            if item.product_with_price_ref not in most_sold_items:
                p_sale_detail = {"quantity":item.quantity, "product_amount": item.quantity * item.unit_sell_price}
                p_sale_detail["profit"] = p_sale_detail["product_amount"] - item.quantity * item.product_with_price_ref.cost_price
                p_sale_detail["profit_percent"] = round((p_sale_detail["profit"] / p_sale_detail["product_amount"]) * 100, 2)
                
                most_sold_items.update({item.product_with_price_ref:p_sale_detail})
            else:
                p_sale_detail = {"quantity":item.quantity, "product_amount": item.quantity * item.unit_sell_price}
                p_sale_detail["profit"] = p_sale_detail["product_amount"] - item.quantity * item.product_with_price_ref.cost_price
                p_sale_detail["profit_percent"] = round((p_sale_detail["profit"] / p_sale_detail["product_amount"]) * 100, 2)

                existing_p_sale_detail = most_sold_items[item.product_with_price_ref]
                
                existing_p_sale_detail["quantity"] += p_sale_detail["quantity"]
                existing_p_sale_detail["product_amount"] += p_sale_detail["product_amount"]
                existing_p_sale_detail["profit"] += p_sale_detail["profit"]
                existing_p_sale_detail["profit_percent"] = round((existing_p_sale_detail["profit"] / existing_p_sale_detail["product_amount"]) * 100, 2)
            
            sold_amount += p_sale_detail["product_amount"]
            profit +=  p_sale_detail["profit"]
    
    context = {
        "sold_amount" : sold_amount,
        "profit": profit, 
        "most_sold_items": most_sold_items
    }    
    return context