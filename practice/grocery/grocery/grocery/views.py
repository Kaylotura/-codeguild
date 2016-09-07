from django.http import HttpResponse

from . import logic



def get_product_price(request, name):
    try:
        product_price = logic.price_for_product_name(name)
    except KeyError:
        return HttpResponse('Not found', status=404)
    return_statement = name + ' is ' + str(product_price) + ' dollars'
    return HttpResponse(return_statement)

def get_price_in_currency(request, name, currency):
    try:
        usd_price = logic.price_for_product_name(name)
    except KeyError:
        return HttpResponse('Not found', status=404)
    try:
        converted_price = logic.convert_currency(usd_price, currency)
    except ValueError:
        return HttpResponse('Bad request', status=400)
    return_statement = name + ' is ' + str(converted_price) + ' ' + currency
    return HttpResponse(return_statement)
