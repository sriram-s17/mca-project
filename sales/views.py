from django.shortcuts import render, redirect
from database.forms import *
from json import dumps

# Create your views here.
# def sales(request):
#     sales_data = Sales.objects.all()
#     sales_list = []
#     for sale in sales_data:
#         sales_list.append({"id":sale.id, 
#                                "sold_date":sale.sold_date, 
#                                "customer_ref":sale.customer_ref,
#                                "total_amount": sale.total_amount,
#                                "last_sale_from_supplier": False})
        
#     sale_payments = SalePayments.objects.all()
#     if sale_payments:
#         for sale in sales_list:
#             payments = sale_payments.filter(sale_ref = sale["id"])
#             pamount = 0
#             for payment in payments:
#                 pamount += payment.paid_amount
#             sale["paid_amount"] = pamount

#             if sales_data.filter(customer_ref=sale["customer_ref"]).last().id == sale["id"]:
#                 sale["last_sale_from_supplier"] = True
#                 sale["balance_amount"] = payments.last().balance_amount

#     context = {
#         "sales":sales_list
#     }

#     return render(request, 'sales.html', context)

# def viewsale(request, id):
#     sale = Sales.objects.get(id = id)
#     sale_details = SaleDetails.objects.filter(sale_ref = id)
#     sale_payments = SalePayments.objects.filter(sale_ref = id)
#     context = {
#         "sale":sale,
#         "prev_balance": sale.total_amount - sale.bill_amount,
#         "last_purch_from_this_sup": True,
#         "sale_details": sale_details
#     }
#     last_purch_from_this_sup = Sales.objects.filter(customer_ref=sale.customer_ref).last()
#     if sale.id < last_purch_from_this_sup.id:
#         context["last_purch_from_this_sup"] = False

#     if sale_payments:
#         context["sale_payments"] = sale_payments
#         context["balance_amount"] = sale_payments.last().balance_amount
#         pamount = 0
#         damount = 0
#         for sale_payment in sale_payments:
#             pamount += sale_payment.paid_amount
#             damount += sale_payment.discounted_amount
#         context["paid_amount"] = pamount
#         context["discounted_amount"] = damount
#     return render(request, "view_sale.html", context)

# def addsale(request):
#     context = {
#         'customer_ref_form': CustomerRefForm,
#         'sale_detail_add_form': SaleDetailsForm,
#         'product_selling_prices': dumps(dict(ProductDetails.objects.all().values_list('id','selling_price')))
#     }
#     if request.method == "POST":
#         prev_sale = Sales.objects.filter(customer_ref_id = request.POST["customer_ref"]).last()
#         balance = 0
#         if prev_sale:
#             prev_sale_payment = SalePayments.objects.filter(sale_ref_id=prev_sale.id).last()
#             if prev_sale_payment:
#                 balance = prev_sale_payment.balance_amount
#             else:
#                 balance = prev_sale.total_amount
#         new_sale = Sales(customer_ref_id=request.POST["customer_ref"], bill_amount=request.POST["total_amt"], total_amount=int(request.POST["total_amt"])+balance)
#         new_sale.save()

#         f_product_detail_ref = request.POST.getlist("product_detail_ref")
#         f_unit_cost_price = request.POST.getlist("unit_cost_price")
#         f_quantity = request.POST.getlist("quantity")
#         #saving sale details i.e saving each products sold in the database
#         if len(f_product_detail_ref)==len(f_product_detail_ref)==len(f_product_detail_ref):
#             for i in range(len(f_product_detail_ref)):
#                 new_product_sale = SaleDetails(sale_ref_id=new_sale.id, product_detail_ref_id=f_product_detail_ref[i], unit_cost_price=f_unit_cost_price[i],quantity=f_quantity[i])
#                 new_product_sale.save()

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
                    
#             return redirect(addpayment, new_sale.id)
#     return render(request, 'add_sale.html', context)

# def addpayment(request, id):
#     sale_ref = Sales.objects.get(id=id)
#     context = {
#         "sale_ref":sale_ref,
#         "balance":sale_ref.total_amount
#     }

#     sale_payments = SalePayments.objects.filter(sale_ref_id=id)
#     if sale_payments:
#         pamount = 0
#         damount = 0
#         for sale_payment in sale_payments:
#             pamount += sale_payment.paid_amount
#             damount += sale_payment.discounted_amount
#         context["paid_amount"] = pamount
#         context["discounted_amount"] = damount
#         context["balance"] = sale_payments.last().balance_amount
#     p_balance = context["balance"]
#     if request.method == "POST":
#         f_discounted_amount = 0
#         if request.POST["discounted_amount"]:
#             f_discounted_amount = request.POST["discounted_amount"]
#         new_payment = SalePayments(sale_ref_id=id, paid_amount=request.POST["paid_amount"], discounted_amount=f_discounted_amount, balance_amount = p_balance - (int(f_discounted_amount) + int(request.POST["paid_amount"])))
#         new_payment.save()
#         return redirect(addpayment, id)
#     return render(request, "add_payment.html", context)