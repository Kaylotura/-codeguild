from .models import PRODUCTS
from .models import CONVERSION_RATES

def price_for_product_name(name):
    product_price = [
        product['price_dollars']
        for product in PRODUCTS
        if product['name'] == name]
    if len(product_price) == 0:
        raise KeyError('Product not found')
    return product_price[0]

def convert_currency(in_amount, out_currency):
    try:
        return in_amount * CONVERSION_RATES[out_currency]
    except KeyError:
        raise ValueError('Invalid currency')
