from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from database.forms import *
from django.forms import modelformset_factory
from json import dumps
import pprint
# Create your views here.
class ViewStocks(View):
    def get(self, request):
        stock_details = StockDetail.objects.order_by("product_detail_ref", "warehouse_ref")
        stock_details_dict = {stock_details[0].product_detail_ref:{}}
        for stock in stock_details:
            if stock.product_detail_ref in stock_details_dict:
                stock_details_dict[stock.product_detail_ref].update({stock.warehouse_ref_id:stock.quantity})
            else:
                stock_details_dict.update({stock.product_detail_ref:{stock.warehouse_ref_id:stock.quantity}})
        warehouses = Warehouse.objects.all()
        context = {
            "product_stocks": stock_details_dict,
            "warehouses": warehouses
        }
        
        return render(request, 'stocks.html', context)

class EditStock(View):
    def get(self, request):
        if request.GET.get("pdid", None):
            context = {
                'stock_form': StockDetailForm(initial={'product_detail_ref':request.GET["pdid"]})
            }
            stock = StockDetail.objects.filter(product_detail_ref=request.GET["pdid"])
            if stock:
                available_stock = stock[0].quantity
                context["available_stock"] = available_stock
        else:
            context = {'stock_form': StockDetailForm}
        return render(request, "edit_stock.html", context)

    def post(self, request):
        stock_detail = StockDetail.objects.filter(warehouse_ref=request.POST["warehouse_ref"], product_detail_ref=request.POST["product_detail_ref"])
        if stock_detail:
            stock_detail.update(quantity = stock_detail[0].quantity+(int(request.POST["quantity"])))
        else:
            stock_form_data = StockDetailForm(request.POST)
            stock_form_data.save()
        return redirect("view_stocks")
    
def get_quantity(request):
    wid = request.GET.get("wid", None)
    pdid = request.GET.get("pdid",None)
    if wid and pdid:
        stocks = StockDetail.objects.filter(warehouse_ref=wid, product_detail_ref=pdid)
        if stocks:
            quantity = stocks[0].quantity
        else:
            quantity = 0
        return JsonResponse(quantity, safe=False)
    else:
        return JsonResponse("",safe=False)
    
class TransferStock(View):
    def get(self, request):
        context = {
            'product_select_form':ProductSelectForm,
            'transfer_stock_form':TransferStockForm
        }
        pdid = request.GET.get("pdid", None)
        if pdid:
            context["product_select_form"] = ProductSelectForm(initial={'product_detail_ref':pdid})
        
        return render(request, "transfer_stock.html", context)
    def post(self, request):
        pdid = request.POST["product_detail_ref"]
        from_warehouse_id = request.POST["from_warehouse_ref"]
        quantity = int(request.POST["quantity"])
        if quantity > 0:
            from_stock_detail = StockDetail.objects.get(warehouse_ref=from_warehouse_id, product_detail_ref=pdid)
            from_stock_detail.quantity = from_stock_detail.quantity - quantity
            from_stock_detail.save()
            to_warehouse_id = request.POST["warehouse_ref"]
            to_stock_detail = StockDetail.objects.filter(warehouse_ref = to_warehouse_id, product_detail_ref = pdid)
            if to_stock_detail:
                to_stock_detail.update(quantity = to_stock_detail[0].quantity+quantity)
            else:
                new_stock_detail = StockDetail(warehouse_ref_id= to_warehouse_id, product_detail_ref_id = pdid, quantity = quantity)
                new_stock_detail.save()
        return redirect("view_stocks")

def get_warehouse_and_quantity(request):
    pdid = request.GET.get("pdid", None)
    if pdid:
        stock_details = StockDetail.objects.filter(product_detail_ref=pdid)
        if stock_details:
            stock_details_dict = {}
            i=0
            for stock_detail in stock_details:
                stock_details_dict.update({i:{"warehouse":
                                                {"id": stock_detail.warehouse_ref_id,
                                                "name": stock_detail.warehouse_ref.__str__()}, 
                                            "quantity":stock_detail.quantity}})
                i+=1

            return JsonResponse(dumps(stock_details_dict), safe=False)
    else:
        return JsonResponse('', safe=False)