from django import template
register = template.Library()

@register.filter
def quantity(dict, key):
    return dict[key]["quantity"]

@register.filter
def status(dict, key):
    return dict[key]["status"]

@register.filter
def keyvalue(dict, key):
    return dict[key]

@register.filter
def mul(value, multiplier):
    return value*multiplier

@register.filter
def getstock(stocks, warehouse_id):
    matching_stock = None
    for stock in stocks:
        if stock["warehouse_id"] == warehouse_id:
            matching_stock = stock
    return matching_stock