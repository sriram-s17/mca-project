from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from database.forms import *
from json import dumps
from user.views import GroupRequiredMixin


def get_sale_detail(sale, get_payments=True, get_items=True):
    context = {
            "sale_ref":sale,
            "total_amount":sale.bill_amount - sale.discount_amount,
            "paid_amount": 0,
            "balance_amount": sale.bill_amount - sale.discount_amount
    }
    if get_items:
        sale_items = SaleItem.objects.filter(sale_ref = sale)
        context["sale_items"] = sale_items
    
    sale_payments = SalePayment.objects.filter(sale_ref = sale)
    if sale_payments:
        if get_payments:
            context["sale_payments"] = sale_payments
        pamount = 0
        for payment in sale_payments:
            pamount += payment.paid_amount
        context["paid_amount"] = pamount
        context["balance_amount"] = sale_payments.last().balance_amount
    
    return context

# Create your views here.
class ViewSales(GroupRequiredMixin, View):
    groups_required = ['Owner', 'Salesman']
    def get(self, request):
        sales = SaleHeaderDetail.objects.all()
        sales_list = []
        for sale in sales:
            sales_list.append(get_sale_detail(sale, False, False))

        context = {
            "sales":sales_list
        }

        return render(request, 'sales.html', context)

class ViewSale(GroupRequiredMixin, View):
    groups_required = ['Owner', 'Salesman']
    def get(self, request, id):
        sale = SaleHeaderDetail.objects.filter(sale_id = id).first()
        if sale:
            context = get_sale_detail(sale)
        else:
            return redirect('view_sales')

        return render(request, "view_sale.html", context)

def get_stock_detail_with_price():
    stocked_products = StockDetail.objects.filter(quantity__gt=0, status="good")
    stocked_product_price_refs = []
    for stock in stocked_products:
        stocked_product_price_refs.append({stock.product_with_price_ref_id:float(stock.product_with_price_ref.selling_price)})
    return stocked_product_price_refs

class AddSale(GroupRequiredMixin, View):
    groups_required = ['Owner', 'Salesman']
    def get(self, request):
        context = {
            'sale_header_form': SaleHeaderForm,
            'sale_item_form': SaleItemForm,
            'product_prices': dumps(get_stock_detail_with_price())
        }
        customer = request.GET.get("cid", None)
        if customer:
            context["sale_header_form"] = SaleHeaderForm(initial={'customer_ref': customer})
        return render(request, 'add_sale.html', context)

    def post(self, request):
        
        product_price_refs = request.POST.getlist("product_with_price_ref")
        sell_price_data = request.POST.getlist("unit_sell_price")
        quantity_data = request.POST.getlist("quantity")

        bill_amount = 0
        for i in range(len(product_price_refs)): 
            bill_amount += int(quantity_data[i])*float(sell_price_data[i])

        discount_percent = float(request.POST.get("discount_percent", 0))
        discount_amount = int(request.POST.get("discount_amount", 0))
        new_sale = SaleHeaderDetail(customer_ref_id = request.POST["customer_ref"], 
                                    bill_amount = bill_amount, 
                                    discount_percent = discount_percent, 
                                    discount_amount = discount_amount)
        new_sale.save()

        #saving each sold products items in the database
        for i in range(len(product_price_refs)):
            new_sale_item = SaleItem(sale_ref_id = new_sale.sale_id, 
                                     product_with_price_ref_id = product_price_refs[i], 
                                     unit_sell_price = sell_price_data[i],
                                     quantity = quantity_data[i])
            new_sale_item.save()
                
            #updating stock
            product_stock =  StockDetail.objects.filter(product_with_price_ref = product_price_refs[i], warehouse_ref_id =1, status="good").first()
            if product_stock:
                if product_stock.quantity - int(quantity_data[i]) == 0:
                    product_stock.delete()
                else:
                    product_stock.quantity -= int(quantity_data[i])
                    product_stock.save()
                    
        return redirect("view_sale", new_sale.sale_id)

class RecordPayment(GroupRequiredMixin, View):
    groups_required = ['Owner', 'Salesman']
    def get(self, request, id):
        sale = SaleHeaderDetail.objects.filter(sale_id=id).first()
        if sale:
            context = get_sale_detail(sale, False, False)
        else:
            return redirect('view_sales')

        return render(request, "record_sale_payment.html", context)
    
    def post(self, request, id):
        paid_amount = float(request.POST["paid_amount"])
        last_payment = SalePayment.objects.filter(sale_ref_id=id).last()
        if last_payment:
            balance = last_payment.balance_amount
        else:
            sale_ref = SaleHeaderDetail.objects.get(sale_id=id)
            balance = sale_ref.bill_amount - sale_ref.discount_amount

        if balance > 0:
            new_payment = SalePayment(sale_ref_id=id, 
                                        paid_amount= paid_amount,
                                        balance_amount = float(balance) - paid_amount)
            new_payment.save()
        return redirect("view_sale", id)
    