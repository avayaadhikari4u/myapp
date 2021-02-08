from django.shortcuts import render,HttpResponse,redirect
from store.models.customer import Customer
from django.contrib import messages
from django.views import View
class Customer_profile(View):
    def get(self,request):
        customer_id=request.session.get('customer')
        cus_id=[]
        cus_id.append(customer_id)
        customers = Customer.get_customer_by_id(cus_id)
        print(customers)
        dec={}
        dec['customers']=customers
        print(dec)
        #dec['categories']=categories
        return render(request,'customer_id.html',dec)
        
