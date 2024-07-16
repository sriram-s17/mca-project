from django.shortcuts import render, redirect
from django.views import View
from database.models import *
from database.forms import ProductDetailSelectForm, CustomerSelectForm
from django.utils import timezone
import calendar
from user.views import GroupRequiredMixin

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Create your views here.
class MonthlyReport(GroupRequiredMixin, View):
    def get(self, request):
        requested_period = request.GET.get("month_year", None)
        default_period = request.GET.get("default", "last 30 days")
        context = {}
        if requested_period:
            year, month = map(lambda x: int(x), requested_period.split("-"))

            from_dt = timezone.datetime(year, month, 1, 0, 0, tzinfo=timezone.get_current_timezone())
            
            to_dt = timezone.datetime(year, month, calendar.monthrange(year, month)[1], 0, 0, tzinfo=timezone.get_current_timezone())
            period = months[month-1] + " " + str(year)
            sales = SaleHeaderDetail.objects.filter(sold_date__range=(from_dt, to_dt))
        elif default_period:
            if default_period == "last 30 days":
                period = default_period
                sales = SaleHeaderDetail.objects.filter(sold_date__gte=timezone.now()-timezone.timedelta(days=30))
        context = monthly_profit_of_sales(sales)
        context.update({"period":period})
        
        return render(request, "monthly_wise_report.html", context)
    
def monthly_profit_of_sales(sales):
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

class ProductWiseReport(View):
    def get(self, request):
        pdid = request.GET.get("product_detail_ref")
        context = {}
        if pdid:
            context = sales_report_of_product(pdid)
            context["product"] = ProductDetail.objects.filter(product_detail_id=pdid).first()
        context["product_detail_select_form"] = ProductDetailSelectForm
        return render(request, "product_wise_report.html", context)
    
def sales_report_of_product(pdid):
    product_prices = ProductPrice.objects.filter(product_detail_ref_id = pdid)
    ppids = [pp.product_price_id for pp in product_prices]

    sold_amount = 0
    profit_amount = 0
    product_report = {}

    sold_of_ppids = SaleItem.objects.filter(product_with_price_ref__in=ppids)
    for sold in sold_of_ppids:
        period =  f"{months[sold.sale_ref.sold_date.month - 1]} {sold.sale_ref.sold_date.year}"
        if period not in product_report:
            ppid_sold_detail = {"quantity":sold.quantity, "sold_amount":sold.quantity * sold.unit_sell_price }
            ppid_sold_detail["profit"] = ppid_sold_detail["sold_amount"] - sold.quantity * sold.product_with_price_ref.cost_price
            ppid_sold_detail["profit_percent"] = round((ppid_sold_detail["profit"] / ppid_sold_detail["sold_amount"]) * 100, 2)
            product_report.update({period:ppid_sold_detail})
        else:
            ppid_sold_detail = {"quantity":sold.quantity, "sold_amount": sold.quantity * sold.unit_sell_price}
            ppid_sold_detail["profit"] = ppid_sold_detail["sold_amount"] - sold.quantity * sold.product_with_price_ref.cost_price
            ppid_sold_detail["profit_percent"] = round((ppid_sold_detail["profit"] / ppid_sold_detail["sold_amount"]) * 100, 2)

            existing_ppid_sold_detail = product_report[period]
            
            existing_ppid_sold_detail["quantity"] += ppid_sold_detail["quantity"]
            existing_ppid_sold_detail["sold_amount"] += ppid_sold_detail["sold_amount"]
            existing_ppid_sold_detail["profit"] += ppid_sold_detail["profit"]
            existing_ppid_sold_detail["profit_percent"] = round((existing_ppid_sold_detail["profit"] / existing_ppid_sold_detail["sold_amount"]) * 100, 2)

        sold_amount += ppid_sold_detail["sold_amount"]
        profit_amount +=  ppid_sold_detail["profit"]
    
    sorted_product_report_keys = sorted(product_report.keys(), key=lambda key: months.index(key.split(" ")[0]))
    print(sorted_product_report_keys)
    product_report = {key: product_report[key] for key in sorted_product_report_keys}
    print(product_report)
    context = {
        "sold_amount" : sold_amount,
        "profit_amount": profit_amount, 
        "product_report": product_report
    }
    return context

class CustomerWiseReport(View):
    def get(self, request):
        cid = request.GET.get("customer_ref")
        context = {}
        if cid:
            context = sales_report_of_customer(cid)
            context["customer"] =  Customer.objects.filter(customer_id = cid).first()
        context["customer_select_form"] = CustomerSelectForm
        return render(request, "customer_wise_report.html", context)
    
def sales_report_of_customer(cid):
    sales = SaleHeaderDetail.objects.filter(customer_ref_id = cid)

    sold_amount = 0
    profit_amount = 0
    customer_report = {}

    for sale in sales:
        # sold_amount += sale.bill_amount
        sale_items = SaleItem.objects.filter(sale_ref=sale)
        for item in sale_items:
            if item.product_with_price_ref not in customer_report:
                p_sale_detail = {"quantity":item.quantity, "product_amount": item.quantity * item.unit_sell_price}
                p_sale_detail["profit"] = p_sale_detail["product_amount"] - item.quantity * item.product_with_price_ref.cost_price
                p_sale_detail["profit_percent"] = round((p_sale_detail["profit"] / p_sale_detail["product_amount"]) * 100, 2)
                
                customer_report.update({item.product_with_price_ref:p_sale_detail})
            else:
                p_sale_detail = {"quantity":item.quantity, "product_amount": item.quantity * item.unit_sell_price}
                p_sale_detail["profit"] = p_sale_detail["product_amount"] - item.quantity * item.product_with_price_ref.cost_price
                p_sale_detail["profit_percent"] = round((p_sale_detail["profit"] / p_sale_detail["product_amount"]) * 100, 2)

                existing_p_sale_detail = customer_report[item.product_with_price_ref]
                
                existing_p_sale_detail["quantity"] += p_sale_detail["quantity"]
                existing_p_sale_detail["product_amount"] += p_sale_detail["product_amount"]
                existing_p_sale_detail["profit"] += p_sale_detail["profit"]
                existing_p_sale_detail["profit_percent"] = round((existing_p_sale_detail["profit"] / existing_p_sale_detail["product_amount"]) * 100, 2)
            
            sold_amount += p_sale_detail["product_amount"]
            profit_amount +=  p_sale_detail["profit"]
    
    context = {
        "sold_amount" : sold_amount,
        "profit_amount": profit_amount, 
        "customer_report": customer_report
    }  
    return context