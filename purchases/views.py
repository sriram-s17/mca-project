from django.shortcuts import render, redirect
from django.views import View
from database.forms import *
# Create your views here.
class ViewPurchases(View):
    def get(self, request):
        purchases = PurchaseHeaderDetail.objects.all()
        purchases_list = []
        for purchase in purchases:
            purchases_list.append({"id":purchase.purchase_id, 
                                "purchased_date":purchase.purchased_date, 
                                "supplier_ref":purchase.supplier_ref,
                                "total_amount": purchase.total_amount,
                                "last_pur_from_supplier": False})
            
        for purchase in purchases_list:
            payments = PurchasePayment.objects.filter(purchase_ref = purchase["id"])
            pamount = 0
            for payment in payments:
                pamount += payment.paid_amount
            purchase["paid_amount"] = pamount

            if purchases.filter(supplier_ref=purchase["supplier_ref"]).last().purchase_id == purchase["id"]:
                purchase["last_pur_from_supplier"] = True
                if payments:
                    purchase["balance_amount"] = payments.last().balance_amount
                else:
                    purchase["balance_amount"] = purchase["total_amount"]

        context = {
            "purchases":purchases_list
        }

        return render(request, 'purchases.html', context)

class ViewPurchaseDetail(View):
    def get(self, request, id):
        purchase = PurchaseHeaderDetail.objects.get(purchase_id = id)
        purchased_items = PurchaseItem.objects.filter(purchase_ref = id)
        purchase_payments = PurchasePayment.objects.filter(purchase_ref = id)
        context = {
            "purchase":purchase,
            "prev_balance": purchase.total_amount - purchase.bill_amount,
            "last_pur_from_supplier": False,
            "purchased_items": purchased_items
        }

        if purchase_payments:
            context["purchase_payments"] = purchase_payments
            pamount = 0
            for payment in purchase_payments:
                pamount += payment.paid_amount
            context["paid_amount"] = pamount
            
        last_purchase_id = PurchaseHeaderDetail.objects.filter(supplier_ref=purchase.supplier_ref).last().purchase_id
        if purchase.purchase_id == last_purchase_id:
            context["last_pur_from_supplier"] = True
            if purchase_payments:
                context["balance_amount"] = purchase_payments.last().balance_amount
            else:
                context["balance_amount"] = purchase.total_amount

        return render(request, "view_purchase.html", context)

class AddPurchase(View):
    def get(self, request):
        return render(request, 'add_purchase.html', {'purchase_header_form': PurchaseHeaderForm, 'purchase_item_form': PurchaseItemForm })

    def post(self, request):
        prev_purchase = PurchaseHeaderDetail.objects.filter(supplier_ref_id = request.POST["supplier_ref"]).last()
        balance = 0
        if prev_purchase:
            prev_purchase_payment = PurchasePayment.objects.filter(purchase_ref=prev_purchase).last()
            if prev_purchase_payment:
                balance = prev_purchase_payment.balance_amount
            else:
                balance = prev_purchase.total_amount
        
        prod_detail_ref_data = request.POST.getlist("product_detail_ref")
        cost_price_data = request.POST.getlist("unit_cost_price")
        quantity_data = request.POST.getlist("quantity")

        bill_amount = 0
        for i in range(len(prod_detail_ref_data)): 
            bill_amount += int(quantity_data[i])*int(cost_price_data[i])

        new_purchase = PurchaseHeaderDetail(supplier_ref_id=request.POST["supplier_ref"], bill_amount=bill_amount, total_amount=bill_amount+balance)
        new_purchase.save()

        #saving each purchased products items in the database
        for i in range(len(prod_detail_ref_data)):
            new_purchase_item = PurchaseItem(purchase_ref_id=new_purchase.purchase_id, product_detail_ref_id=prod_detail_ref_data[i], unit_cost_price=cost_price_data[i],quantity=quantity_data[i])
            new_purchase_item.save()
                
            #updating stock
            product_stock =  StockDetail.objects.filter(product_detail_ref=prod_detail_ref_data[i])
            if product_stock:
                product_stock =  product_stock.first()
                product_stock.quantity += int(quantity_data[i])
                product_stock.save()
            else:
                new_stock = StockDetail(product_detail_ref_id=prod_detail_ref_data[i], quantity=quantity_data[i])
                new_stock.save()
                    
        return redirect("view_purchase", new_purchase.purchase_id)

class AddPayment(View):
    def get(self, request, id):
        purchase_ref = PurchaseHeaderDetail.objects.get(purchase_id=id)
        context = {
            "purchase_ref":purchase_ref,
            "prev_balance": purchase_ref.total_amount - purchase_ref.bill_amount,
            "paid_amount": 0,
            "balance": purchase_ref.total_amount
        }

        purchase_payments = PurchasePayment.objects.filter(purchase_ref_id=id)
        if purchase_payments:
            pamount = 0
            for purchase_payment in purchase_payments:
                pamount += purchase_payment.paid_amount
            context["paid_amount"] = pamount
            context["balance"] = purchase_payments.last().balance_amount
        return render(request, "add_payment.html", context)
    
    def post(self, request, id):
        purchase_ref = PurchaseHeaderDetail.objects.get(purchase_id=id)
        balance = purchase_ref.total_amount
        last_payment = PurchasePayment.objects.filter(purchase_ref_id=id).last()
        if last_payment:
            balance = last_payment.balance_amount
        paid_amount = int(request.POST["paid_amount"])
        new_payment = PurchasePayment(purchase_ref_id=purchase_ref.purchase_id, 
                                      paid_amount= paid_amount,
                                      balance_amount = balance - paid_amount)
        new_payment.save()
        return redirect("add_payment", purchase_ref.purchase_id)
    