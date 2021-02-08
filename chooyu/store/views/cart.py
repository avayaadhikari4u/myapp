from store.models.customer import Customer
from store.models.product import Product
from django.shortcuts import render,HttpResponse,redirect
from django.views import View
class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(ids,products)
        return render(request,'cart.html',{'products':products})

   