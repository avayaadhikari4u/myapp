from django.contrib import admin
from .models.product import Product
from .models.category import Category,SubCategory,Brand
from .models.customer import Customer
from .models.orders import Orders
from .models.cart import Cart

# Register your models here.


class AdminSubCategory(admin.ModelAdmin):
    search_fields=('name',)
    list_display=['name','category']

class AdminBrand(admin.ModelAdmin):
    search_fields=('name__exact',)
    list_display=['name','subcategory','category']


class AdminProduct(admin.ModelAdmin):
    search_fields=('name',)
    list_display=['name','price','brand','subcategory','category']
    prepopulated_fields={'slug':('name',)}

class AdminCustomer(admin.ModelAdmin):
    list_display=['email','phone']



admin.site.register(Product,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Orders)
admin.site.register(Cart)
admin.site.register(SubCategory,AdminSubCategory)
admin.site.register(Brand,AdminBrand)
