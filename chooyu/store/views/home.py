from django.shortcuts import render,HttpResponse,redirect
from store.models.product import Product
from store.models.category import Category,SubCategory,Brand
from django.contrib import messages
from django.views import View

# Create your views here.
class Index(View):
    def post(self,request):
        product=request.POST.get('product')
        
        remove=request.POST.get('remove')

        remove_all=request.POST.get('remove_all')
        
        print("love you",remove)
        cart = request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1

                elif remove_all:
                    if quantity>=1:
                        cart.pop(product)

                else:                   
                    cart[product] = quantity+1

            else:
                cart[product]=1

        else:
            cart={}
            cart[product]=1
            
        request.session['cart']=cart
        print(request.session['cart'])
        return redirect("homepage")

    def get(self,request):
        dec={}
        cart=request.session.get('cart')

        if not cart:
            request.session.cart={}
        products= None
        categories = Category.get_all_categories()
        subcategories = SubCategory.get_all_subcategories()
        brands = Brand.get_all_Brand()
        categoryID = request.GET.get('category')
        subcategoryID = request.GET.get('subcategory')
        brandID = request.GET.get('brand')
        print("id is:",brandID)
        
        if categoryID:
           
            subcategories = SubCategory.get_all_subCategory_by_categoryid(categoryID)
            dec['categories']=categories
            dec['subcategories']=subcategories
            return render(request,'index.html',dec)
            #products=Product.get_all_products_by_categoryid(categoryID)
    
        elif subcategoryID:
            dec['categories']=categories
            brands=Brand.get_all_Brands_by_subcategoryid(subcategoryID)
            dec['brands']=brands
            return render(request,'index.html',dec)

        elif brandID:
            dec['categories']=categories
            products=Product.get_all_products_by_brandid(brandID)
            dec['products']=products
            return render(request,'index.html',dec)
        else:
            products = Product.get_all_products()
            print(products)
        dec['products']=products
        dec['categories']=categories
        #dec['brands']=brands
        return render(request,'index.html',dec)
       
def Subcategory(request):
    categories = Category.get_all_categories()
    subcategories = Sub_Category.get_all_subcategories()
    dec={}
    categoryID = request.GET.get('category')
    if categoryID:
        subcategories = Sub_Category.get_all_subCategory_by_categoryid(categoryID)
        #products=Product.get_all_products_by_categoryid(categoryID)
    else:   
        products = Product.get_all_products()
    dec['categories']=categories
    dec['subcategories']=subcategories
    return render(request,'subcategory.html',dec)
 
def contact(request):
    categories = Category.get_all_categories()
    products = Product.get_all_products()
    dec={}
    dec['categories']=categories
    #dec['products']=products
    print(categories)
    return render(request,'contact.html',dec)
    #return render(request,'contact.html')

def about(request):
    return render(request,'about.html')


def order(request):
    return render(request,'order.html')

def emptycart(request):
    categories = Category.get_all_categories()
    products = Product.get_all_products()
    dec={}
    dec['categories']=categories
    #dec['products']=products
    print(categories)
    return render(request,'empty.html',dec)

def search(request):
    query=request.GET['query']
    print(query)
    if query:
        if len(query)>70:
            products=[]
        else:
            #products=Product.objects.all()
            products1=Product.objects.filter(name__icontains=query)
            products2=Product.objects.filter(description__icontains=query)
            products=products1.union(products2)
            print(products)
        if len(products)==0:
            messages.error(request,"please fill the form correctly")
        params={'products':products,'query':query}
        return render(request,"search.html",params)
    else:
        return redirect('homepage')

def profil_prp(request):
    iqre=request.GET['iqre']
    product_list=[]
    iqre=int(iqre)
    product_list.append(iqre)
    categories = Category.get_all_categories()
    products = Product.get_products_by_id(product_list)
    print(products)
    dec={}
    dec['categories']=categories
    dec['products']=products
    #prop={'products':products}
    return render(request,'profil_prp.html',dec)
    






