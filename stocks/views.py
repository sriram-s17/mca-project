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
        stock_details = StockDetail.objects.order_by("product_with_price_ref", "warehouse_ref")
        stock_details_dict = {}
        for stock in stock_details:
            if stock.product_with_price_ref in stock_details_dict:
                if stock.status in stock_details_dict[stock.product_with_price_ref]:
                    stock_details_dict[stock.product_with_price_ref][stock.status].append({"warehouse_id":stock.warehouse_ref_id, "quantity":stock.quantity})
                else:
                    stock_details_dict[stock.product_with_price_ref][stock.status] = [{"warehouse_id":stock.warehouse_ref_id, "quantity":stock.quantity}]
            else:
                stock_details_dict.update({stock.product_with_price_ref:{stock.status: [{"warehouse_id":stock.warehouse_ref_id, "quantity":stock.quantity}]}})
        warehouses = Warehouse.objects.all()
        pprint.pprint(stock_details_dict)
        context = {
            "product_stocks": stock_details_dict,
            "warehouses": warehouses
        }
        
        return render(request, 'stocks.html', context)

def get_quantity(request):
    wid = request.GET.get("wid", 1)
    ppid = request.GET.get("ppid",None)
    if ppid:
        stock = StockDetail.objects.filter(product_with_price_ref = ppid, warehouse_ref_id = wid, status="good").first()
        if stock:
            quantity = stock.quantity
        else:
            quantity = 0
        return JsonResponse(quantity, safe=False)
    else:
        return JsonResponse("",safe=False)

class EditStock(View):
    def get(self, request):
        context = {
            'stock_form': StockDetailForm,
        }
        ppid = request.GET.get("ppid", None)
        if ppid:
            stock_detail = StockDetail.objects.filter(warehouse_ref=1, product_with_price_ref=ppid).first()
            context['stock_form'] = StockDetailForm(instance=stock_detail)
        return render(request, "edit_stock.html", context)

    def post(self, request):
        status = request.POST["status"]
        quantity = request.POST["quantity2"]
        w_ref = request.POST["warehouse_ref"]
        pp_ref = request.POST["product_with_price_ref"]
        stock_detail = StockDetail.objects.filter(warehouse_ref=w_ref, product_with_price_ref=pp_ref, status = status).first()
        if stock_detail:
            #for saving if the record already available , it is common for all status
            stock_detail.quantity += int(quantity)
            stock_detail.save()
        else:
            new_stock = StockDetail(warehouse_ref_id=w_ref, product_with_price_ref_id=pp_ref, quantity=quantity, status=status)
            new_stock.save()
        if status != "good":
            good_stock = StockDetail.objects.filter(warehouse_ref=w_ref, product_with_price_ref=pp_ref, status = "good").first()
            good_stock.quantity -=  int(quantity)
            good_stock.save()

        return redirect("view_stocks")
    
class TransferStock(View):
    def get(self, request):
        context = {
            'product_select_form':ProductSelectForm,
            'transfer_stock_form':TransferStockForm
        }
        ppid = request.GET.get("ppid", None)
        if ppid:
            context["product_select_form"] = ProductSelectForm(initial={'product_with_price_ref':ppid})
        
        return render(request, "transfer_stock.html", context)
    def post(self, request):
        ppid = request.POST["product_with_price_ref"]
        from_warehouse_id = request.POST["from_warehouse_ref"]
        quantity = int(request.POST["quantity"])
        if quantity > 0:
            from_stock_detail = StockDetail.objects.get(warehouse_ref=from_warehouse_id, product_with_price_ref=ppid, status="good")
            from_stock_detail.quantity = from_stock_detail.quantity - quantity
            from_stock_detail.save()
            to_warehouse_id = request.POST["warehouse_ref"]
            to_stock_detail = StockDetail.objects.filter(warehouse_ref = to_warehouse_id, product_with_price_ref = ppid, status="good")
            if to_stock_detail:
                to_stock_detail.update(quantity = to_stock_detail[0].quantity+quantity)
            else:
                new_stock_detail = StockDetail(warehouse_ref_id= to_warehouse_id, product_with_price_ref = ppid, quantity = quantity)
                new_stock_detail.save()
        return redirect("view_stocks")

def get_warehouse_and_quantity(request):
    ppid = request.GET.get("ppid", None)
    if ppid:
        stock_details_dict = {}
        stock_details = StockDetail.objects.filter(product_with_price_ref=ppid, status="good")
        if stock_details:
            i=0
            for stock_detail in stock_details:
                stock_details_dict.update({i:{"warehouse":
                                                {"id": stock_detail.warehouse_ref_id,
                                                "name": stock_detail.warehouse_ref.__str__()}, 
                                            "quantity":stock_detail.quantity}})
                i+=1
        if stock_details_dict:
            return JsonResponse(dumps(stock_details_dict), safe=False)
        else:
            return JsonResponse('0', safe=False)
    else:
        return JsonResponse('', safe=False)