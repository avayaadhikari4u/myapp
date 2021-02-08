from django.contrib.auth.hashers import make_password
from django.shortcuts import render,HttpResponse,redirect
from store.models.customer import Customer
from django.contrib import messages
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        postData=request.POST
        first_name=postData.get('FirstName')
        last_name=postData.get('LastName')
        phone=postData.get('Phone')
        email=postData.get('email')
        password=postData.get('password')
        confirm_password=postData.get('ConfirmPassword')
        #valadiation
        value={
            'first_name': first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email
        }

        

        customer=Customer(first_name=first_name,
        last_name=last_name,
        phone=phone,
        email=email,
        password=password,
        confirm_password=confirm_password)
        error_message= self.valadCustomer(customer)
        if not error_message:
            customer.password=make_password(customer.password)
            customer.confirm_password=make_password(customer.confirm_password)
            customer.register()
            messages.success(request,"Signup Success.Please login")
            return redirect('login')
        else:
            data={
                'error' : error_message,
                'values' : value
            }
            return render(request,'signup.html',data)

    def valadCustomer(self,customer):
        error_message=None
        if(not customer.first_name):
            error_message="first name is required:"
        elif len(customer.first_name)<4:
            error_message='first name must be greater then 4 '

        if(not customer.last_name):
            error_message="last name is required:"
        elif len(customer.last_name)<4:
            error_message='last name must be greater then 4 '



        if(not customer.phone):
            error_message="Phone number is required:"
        elif len(customer.phone)<10:
            error_message='Phone Number must be greater then 10 '


        if(not customer.password):
            error_message="fill password:"
        elif len(customer.password)<6:
            error_message='password must be greater then 6 '

        if(not customer.confirm_password):
            error_message="fill password:"
        elif customer.password!=customer.confirm_password:
            error_message='password mismatch'

        
        if customer.isExists():
            error_message='Email already used'

        return error_message