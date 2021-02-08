from django import template
register=template.Library()
@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    print(cart)
    keys=list(cart.keys())
    for id in keys:
        if int(id)==product.id:
            print("this is id=",id)
            return True
    return False

@register.filter(name='quantity_count')
def quantity_count(product,cart):
    keys=list(cart.keys())
    for id in keys:
        if int(id)==product.id:
            return cart.get(id)
    return 0

@register.filter(name='total_price')
def total_price(product,cart):
    return product.price * quantity_count(product,cart)
    
@register.filter(name='total_cart_price')
def total_cart_price(products,cart):
    sum=0
    for p in products:
        sum+=total_price(p,cart)
    return sum
            