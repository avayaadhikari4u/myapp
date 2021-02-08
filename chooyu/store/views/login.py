from django.contrib.auth.hashers import  check_password
from django.shortcuts import render,HttpResponse,redirect
from store.models.customer import Customer
from django.contrib import messages
from django.views import View
class Login(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_user(email)
        print("This is",customer)
        error_message=None
        if customer:
            print(customer.first_name,customer.last_name,customer.id)
            flag = check_password(password,customer.password)
            if flag:
                request.session['customer'] = customer.id

                messages.success(request,"successfully logged In!!")
                return redirect('homepage')
                
            else:
                error_message="password incorrect"
        else:
            error_message="Email invalid"
        return render(request,'login.html',{'error':error_message})


def logout(request):
    request.session.clear()
    return redirect('login')