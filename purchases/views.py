from django.shortcuts import render, redirect
from django.views import View
from database.forms import *
from user.views import GroupRequiredMixin

def get_purchase_detail(purchase, get_payments=True, get_items=True):
    context = {
        "purchase_ref":purchase,
        "paid_amount": 0,
        "balance_amount": purchase.bill_amount
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

    return context

# Create your views here.
class ViewPurchases(GroupRequiredMixin, View):
    def get(self, request):
        purchases = PurchaseHeaderDetail.objects.all()
        purchases_list = []
        for purchase in purchases:
            purchases_list.append(get_purchase_detail(purchase, False, False))

        context = {
            "purchases":purchases_list
        }

        return render(request, 'purchases.html', context)

class ViewPurchaseDetail(GroupRequiredMixin, View):
    def get(self, request, id):
        purchase = PurchaseHeaderDetail.objects.filter(purchase_id = id).first()
        if purchase:
            context = get_purchase_detail(purchase)
            return render(request, "view_purchase.html", context)
        else:
            return redirect("view_purchases")

class AddPurchase(GroupRequiredMixin, View):
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
                old_prices = ProductPrice.objects.filter(product_detail_ref=prod_detail_ref_data[i])
                if old_prices :
                    same_price = old_prices.filter( cost_price=cost_price_data[i]).first()
                    #checks if the product already has the same cost price
                    if  same_price:
                        price_ref = same_price
                    else:
                        has_cost_zero = old_prices.filter(cost_price=0).first()
                        #checks if the product's price record has cost price 0, 
                        #bcoz when we create product and add it first time in purchase, the cost price is zero
                        if has_cost_zero:
                            has_cost_zero.cost_price = cost_price_data[i]
                            has_cost_zero.save()
                            price_ref = has_cost_zero
                        else:
                            #if the product has no same price and also has no 0 cost price, then it can be a new price, so we need to add a new record, with the same last selling price
                            last_price = old_prices.order_by("updated_date").last()
                            new_price = ProductPrice(product_detail_ref_id=prod_detail_ref_data[i] ,cost_price=cost_price_data[i], selling_price=last_price.selling_price)
                            new_price.save()
                            price_ref = new_price
                else:
                    #add new price record, when the product has no price record, but it is not possible bcoz we already required selling price when we add product
                    #but for emergency, it is used
                    new_price = ProductPrice(product_detail_ref_id=prod_detail_ref_data[i] ,cost_price=cost_price_data[i])
                    new_price.save()
                    price_ref = new_price
                    

            #updating stock
            if price_ref:
                product_stock =  StockDetail.objects.filter(product_with_price_ref=price_ref, warehouse_ref=1).first()
                if product_stock:
                    product_stock.quantity += int(quantity_data[i])
                    product_stock.save()
                else:
                    new_stock = StockDetail(product_with_price_ref=price_ref, quantity=quantity_data[i])
                    new_stock.save()
                    
        return redirect("view_purchase", new_purchase.purchase_id)

class RecordPayment(GroupRequiredMixin, View):
    def get(self, request, id):
        purchase = PurchaseHeaderDetail.objects.filter(purchase_id=id).first()
        if purchase:
            context = get_purchase_detail(purchase, False, False)
            return render(request, "record_purchase_payment.html", context)
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

        return redirect("view_purchase", id)
    