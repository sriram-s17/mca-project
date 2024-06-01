from django.shortcuts import render, redirect
from database.forms import *

# Create your views here.
# def purchases(request):
#     purchases_data = Purchases.objects.all()
#     purchases_list = []
#     for purchase in purchases_data:
#         purchases_list.append({"id":purchase.id, 
#                                "purchased_date":purchase.purchased_date, 
#                                "supplier_ref":purchase.supplier_ref,
#                                "total_amount": purchase.total_amount,
#                                "last_purchase_from_supplier": False})
        
#     purchase_payments = PurchasePayments.objects.all()
#     if purchase_payments:
#         for purchase in purchases_list:
#             payments = purchase_payments.filter(purchase_ref = purchase["id"])
#             pamount = 0
#             for payment in payments:
#                 pamount += payment.paid_amount
#             purchase["paid_amount"] = pamount

#             if purchases_data.filter(supplier_ref=purchase["supplier_ref"]).last().id == purchase["id"]:
#                 purchase["last_purchase_from_supplier"] = True
#                 purchase["balance_amount"] = payments.last().balance_amount

#     context = {
#         "purchases":purchases_list
#     }

#     return render(request, 'purchases.html', context)

# def viewpurchase(request, id):
#     purchase = Purchases.objects.get(id = id)
#     purchase_details = PurchaseDetails.objects.filter(purchase_ref = id)
#     purchase_payments = PurchasePayments.objects.filter(purchase_ref = id)
#     context = {
#         "purchase":purchase,
#         "prev_balance": purchase.total_amount - purchase.bill_amount,
#         "last_purch_from_this_sup": True,
#         "purchase_details": purchase_details
#     }
#     last_purch_from_this_sup = Purchases.objects.filter(supplier_ref=purchase.supplier_ref).last()
#     if purchase.id < last_purch_from_this_sup.id:
#         context["last_purch_from_this_sup"] = False

#     if purchase_payments:
#         context["purchase_payments"] = purchase_payments
#         context["balance_amount"] = purchase_payments.last().balance_amount
#         pamount = 0
#         damount = 0
#         for purchase_payment in purchase_payments:
#             pamount += purchase_payment.paid_amount
#             damount += purchase_payment.discounted_amount
#         context["paid_amount"] = pamount
#         context["discounted_amount"] = damount
#     return render(request, "view_purchase.html", context)

# def addpurchase(request):
#     context = {
#         'supplier_ref_form': SupplierRefForm,
#         'purchase_detail_add_form': PurchaseDetailForm
#     }
#     if request.method == "POST":
#         prev_purchase = Purchases.objects.filter(supplier_ref_id = request.POST["supplier_ref"]).last()
#         balance = 0
#         if prev_purchase:
#             prev_purchase_payment = PurchasePayments.objects.filter(purchase_ref_id=prev_purchase.id).last()
#             if prev_purchase_payment:
#                 balance = prev_purchase_payment.balance_amount
#             else:
#                 balance = prev_purchase.total_amount
#         new_purchase = Purchases(supplier_ref_id=request.POST["supplier_ref"], bill_amount=request.POST["total_amt"], total_amount=int(request.POST["total_amt"])+balance)
#         new_purchase.save()

#         f_product_detail_ref = request.POST.getlist("product_detail_ref")
#         f_unit_cost_price = request.POST.getlist("unit_cost_price")
#         f_quantity = request.POST.getlist("quantity")
#         #saving purchase details i.e saving each products purchased in the database
#         if len(f_product_detail_ref)==len(f_product_detail_ref)==len(f_product_detail_ref):
#             for i in range(len(f_product_detail_ref)):
#                 new_product_purchase = PurchaseDetails(purchase_ref_id=new_purchase.id, product_detail_ref_id=f_product_detail_ref[i], unit_cost_price=f_unit_cost_price[i],quantity=f_quantity[i])
#                 new_product_purchase.save()

#                 #updating stock
#                 stock_of_product =  StockDetails.objects.filter(product_detail_ref=f_product_detail_ref[i])
#                 if len(stock_of_product) == 1:
#                     stock_of_product =  stock_of_product.first()
#                     stock_of_product.quantity += int(f_quantity[i])
#                     stock_of_product.save()
#                 elif not stock_of_product:
#                     new_stock = StockDetails(product_detail_ref_id=f_product_detail_ref[i], quantity=f_quantity[i] )
#                     new_stock.save()
#                 else:
#                     print("stock not updated correctly. something error. length of stock of product", f_product_detail_ref[i], len(stock_of_product) )
                    
#             return redirect(addpayment, new_purchase.id)
#     return render(request, 'add_purchase.html', context)

# def addpayment(request, id):
#     purchase_ref = Purchases.objects.get(id=id)
#     context = {
#         "purchase_ref":purchase_ref,
#         "balance":purchase_ref.total_amount
#     }

#     purchase_payments = PurchasePayments.objects.filter(purchase_ref_id=id)
#     if purchase_payments:
#         pamount = 0
#         damount = 0
#         for purchase_payment in purchase_payments:
#             pamount += purchase_payment.paid_amount
#             damount += purchase_payment.discounted_amount
#         context["paid_amount"] = pamount
#         context["discounted_amount"] = damount
#         context["balance"] = purchase_payments.last().balance_amount
#     p_balance = context["balance"]
#     if request.method == "POST":
#         f_discounted_amount = 0
#         if request.POST["discounted_amount"]:
#             f_discounted_amount = request.POST["discounted_amount"]
#         new_payment = PurchasePayments(purchase_ref_id=id, paid_amount=request.POST["paid_amount"], discounted_amount=f_discounted_amount, balance_amount = p_balance - (int(f_discounted_amount) + int(request.POST["paid_amount"])))
#         new_payment.save()
#         return redirect(addpayment, id)
#     return render(request, "add_payment.html", context)