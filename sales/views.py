from django.shortcuts import render, redirect
from django.views import View
from database.forms import *
from json import dumps

# Create your views here.
class ViewSales(View):
    def get(self, request):
        sales = SaleHeaderDetail.objects.all()
        sales_list = []
        for sale in sales:
            sales_list.append({"id":sale.sale_id, 
                                "sold_date":sale.sold_date, 
                                "customer_ref":sale.customer_ref,
                                "total_amount": sale.total_amount,
                                "last_sale_to_customer": False})
            
        for sale in sales_list:
            payments = SalePayment.objects.filter(sale_ref = sale["id"])
            pamount = 0
            for payment in payments:
                pamount += payment.paid_amount
            sale["paid_amount"] = pamount

            if sales.filter(customer_ref=sale["customer_ref"]).last().sale_id == sale["id"]:
                sale["last_sale_to_customer"] = True
                if payments:
                    sale["balance_amount"] = payments.last().balance_amount
                else:
                    sale["balance_amount"] = sale["total_amount"]

        context = {
            "sales":sales_list
        }

        return render(request, 'sales.html', context)

class ViewSale(View):
    def get(self, request, id):
        sale = SaleHeaderDetail.objects.get(sale_id = id)
        sale_items = SaleItem.objects.filter(sale_ref = id)
        sale_payments = SalePayment.objects.filter(sale_ref = id)
        context = {
            "sale":sale,
            "prev_balance": (sale.total_amount + sale.discount_amount) - sale.bill_amount,
            "sale_items": sale_items,
            "last_sale_to_customer": False  #it is used when we view previous sale of a customer.if it is false, then it is not last sale and 
            # and balance amount is not displayed bcoz their balance amount is added to next sale
            #so we no need to display their display their balance amount
        }

        if sale_payments:
            context["sale_payments"] = sale_payments
            pamount = 0
            for payment in sale_payments:
                pamount += payment.paid_amount
            context["paid_amount"] = pamount
            
        last_sale_id = SaleHeaderDetail.objects.filter(customer_ref=sale.customer_ref).last().sale_id
        if sale.sale_id == last_sale_id:
            context["last_sale_to_customer"] = True
            if sale_payments:
                context["balance_amount"] = sale_payments.last().balance_amount
            else:
                context["balance_amount"] = sale.total_amount

        return render(request, "view_sale.html", context)

class AddSale(View):
    def get(self, request):
        product_details = ProductDetail.objects.all().values_list('prod_detail_id', 'selling_price')
        context = {
            'sale_header_form': SaleHeaderForm,
            'sale_item_form': SaleItemForm,
            'product_details': dumps(dict(product_details))
        }
        customer = request.GET.get("cid", None)
        if customer:
            context["sale_header_form"] = SaleHeaderForm(initial={'customer_ref': Customer.objects.get(customer_id=int(customer))})
        return render(request, 'add_sale.html', context)

    def post(self, request):
        prev_sale = SaleHeaderDetail.objects.filter(customer_ref_id = request.POST["customer_ref"]).last()
        balance = 0
        if prev_sale:
            prev_sale_payment = SalePayment.objects.filter(sale_ref=prev_sale).last()
            if prev_sale_payment:
                balance = prev_sale_payment.balance_amount
            else:
                balance = prev_sale.total_amount
        
        prod_detail_ref_data = request.POST.getlist("product_detail_ref")
        sell_price_data = request.POST.getlist("unit_sell_price")
        quantity_data = request.POST.getlist("quantity")

        bill_amount = 0
        for i in range(len(prod_detail_ref_data)): 
            bill_amount += int(quantity_data[i])*int(sell_price_data[i])

        discount_percent = float(request.POST.get("discount_percent", 0))
        discount_amount = int(request.POST.get("discount_amount", 0))
        new_sale = SaleHeaderDetail(customer_ref_id = request.POST["customer_ref"], 
                                    bill_amount = bill_amount, 
                                    discount_percent = discount_percent, 
                                    discount_amount = discount_amount, 
                                    total_amount = bill_amount - discount_amount + balance)
        new_sale.save()

        #saving each sold products items in the database
        for i in range(len(prod_detail_ref_data)):
            new_sale_item = SaleItem(sale_ref_id = new_sale.sale_id, 
                                     product_detail_ref_id = prod_detail_ref_data[i], 
                                     unit_sell_price = sell_price_data[i],
                                     quantity = quantity_data[i])
            new_sale_item.save()
                
            #updating stock
            product_stock =  StockDetail.objects.filter(product_detail_ref = prod_detail_ref_data[i])
            if product_stock:
                product_stock =  product_stock.first()
                product_stock.quantity -= int(quantity_data[i])
                product_stock.save()
                    
        return redirect("add_sale_payment", new_sale.sale_id)

class AddPayment(View):
    def get(self, request, id):
        sale_ref = SaleHeaderDetail.objects.get(sale_id=id)
        context = {
            "sale_ref":sale_ref,
            "prev_balance": (sale_ref.total_amount + sale_ref.discount_amount) - sale_ref.bill_amount,
            "paid_amount": 0,
            "balance": sale_ref.total_amount
        }

        sale_payments = SalePayment.objects.filter(sale_ref_id=id)
        if sale_payments:
            pamount = 0
            for sale_payment in sale_payments:
                pamount += sale_payment.paid_amount
            context["paid_amount"] = pamount
            context["balance"] = sale_payments.last().balance_amount
        return render(request, "add_sale_payment.html", context)
    
    def post(self, request, id):
        sale_ref = SaleHeaderDetail.objects.get(sale_id=id)
        balance = sale_ref.total_amount
        last_payment = SalePayment.objects.filter(sale_ref_id=id).last()
        if last_payment:
            balance = last_payment.balance_amount
        paid_amount = int(request.POST["paid_amount"])
        new_payment = SalePayment(sale_ref_id=sale_ref.sale_id, 
                                      paid_amount= paid_amount,
                                      balance_amount = balance - paid_amount)
        new_payment.save()
        return redirect("view_sale", sale_ref.sale_id)
    