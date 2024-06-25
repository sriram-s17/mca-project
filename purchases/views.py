from django.shortcuts import render, redirect
from django.views import View
from database.forms import *

def get_purchase_detail(purchase, get_payments=True, get_items=True):
    context = {
        "purchase_ref":purchase
    }
    if get_items:
        purchased_items = PurchaseItem.objects.filter(purchase_ref = purchase)
        context["purchased_items"] = purchased_items
    purchase_payments = PurchasePayment.objects.filter(purchase_ref = purchase)
    if purchase_payments:
        if get_payments:
            context["purchase_payments"] = purchase_payments
        pamount = 0
        for payment in purchase_payments:
            pamount += payment.paid_amount
        context["paid_amount"] = pamount
        context["balance_amount"] = purchase_payments.last().balance_amount
    else:
        context["balance_amount"] = purchase.bill_amount

    return context

# Create your views here.
class ViewPurchases(View):
    def get(self, request):
        purchases = PurchaseHeaderDetail.objects.all()
        purchases_list = []
        for purchase in purchases:
            purchases_list.append(get_purchase_detail(purchase, False, False))

        context = {
            "purchases":purchases_list
        }

        return render(request, 'purchases.html', context)

class ViewPurchaseDetail(View):
    def get(self, request, id):
        purchase = PurchaseHeaderDetail.objects.filter(purchase_id = id).first()
        if purchase:
            context = get_purchase_detail(purchase)
            return render(request, "view_purchase.html", context)
        else:
            return redirect("view_purchases")

class AddPurchase(View):
    def get(self, request):
        return render(request, 'add_purchase.html', {'purchase_header_form': PurchaseHeaderForm, 'purchase_item_form': PurchaseItemForm })

    def post(self, request):
        prod_detail_ref_data = request.POST.getlist("product_detail_ref")
        cost_price_data = request.POST.getlist("unit_cost_price")
        quantity_data = request.POST.getlist("quantity")

        bill_amount = 0
        for i in range(len(prod_detail_ref_data)): 
            bill_amount += int(quantity_data[i])*float(cost_price_data[i])

        new_purchase = PurchaseHeaderDetail(supplier_ref_id=request.POST["supplier_ref"], bill_amount=bill_amount )
        new_purchase.save()

        #saving each purchased products items in the database
        for i in range(len(prod_detail_ref_data)):
            new_purchase_item = PurchaseItem(purchase_ref_id=new_purchase.purchase_id, product_detail_ref_id=prod_detail_ref_data[i], unit_cost_price=cost_price_data[i],quantity=quantity_data[i])
            new_purchase_item.save()

            #updating product price
            if cost_price_data[i]:
                create_price = True
                old_price = ProductPrice.objects.filter(product_detail_ref=prod_detail_ref_data[i]).order_by('updated_date').last() 
                if old_price :
                    if old_price.cost_price == float(cost_price_data[i]):
                        create_price=False
                    if old_price.cost_price==0:
                        create_price = False
                        old_price.cost_price = cost_price_data[i]
                        old_price.save()
                    price_ref = old_price
                if create_price:
                    new_price = ProductPrice(product_detail_ref_id=prod_detail_ref_data[i] ,cost_price=cost_price_data[i], selling_price=old_price.selling_price)
                    new_price.save()
                    price_ref = new_price

            #updating stock
            product_stock =  StockDetail.objects.filter(product_detail_ref=prod_detail_ref_data[i], price_ref=price_ref)
            if product_stock:
                product_stock =  product_stock.first()
                product_stock.quantity += int(quantity_data[i])
                product_stock.save()
            else:
                new_stock = StockDetail(product_detail_ref_id=prod_detail_ref_data[i], price_ref_id=price_ref.product_price_id, quantity=quantity_data[i])
                new_stock.save()
                    
        return redirect("view_purchase", new_purchase.purchase_id)

class AddPayment(View):
    def get(self, request, id):
        purchase = PurchaseHeaderDetail.objects.filter(purchase_id=id).first()
        if purchase:
            context = get_purchase_detail(purchase, False, False)
            return render(request, "add_payment.html", context)
        else:
            return redirect('view_purchases')
    
    def post(self, request, id):
        paid_amount = float(request.POST["paid_amount"])
        last_payment = PurchasePayment.objects.filter(purchase_ref_id=id).last()
        if last_payment:
            balance = last_payment.balance_amount
        else:
            balance = PurchaseHeaderDetail.objects.get(purchase_id=id).bill_amount
        
        if balance > 0:
            new_payment = PurchasePayment(purchase_ref_id=id, 
                                      paid_amount= paid_amount,
                                      balance_amount = float(balance) - paid_amount)
            new_payment.save()

        return redirect("add_payment", id)
    