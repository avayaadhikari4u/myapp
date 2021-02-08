from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Orders
from django.shortcuts import render,HttpResponse,redirect
from django.views import View

class Order(View):
    def get(self,request):
        customer=request.session.get('customer')
        orders=Orders.get_orders_by_customer(customer)
        print(orders)
        return render(request,'orders.html',{'orders':orders})

        