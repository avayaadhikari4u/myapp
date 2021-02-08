from django.db import models
from .category import Category,SubCategory,Brand
import datetime
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    discount=models.IntegerField(default=0)
    description=models.TextField()
    Stock=models.BooleanField(default=True)
    slug=models.SlugField(max_length=100)
    image=models.ImageField(upload_to='uploads/product/')
    image1=models.ImageField(upload_to='uploads/product/')
    image2=models.ImageField(upload_to='uploads/product/')
    date=models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)



    @staticmethod

    def get_all_products():
        return Product.objects.all()


    @staticmethod

    def get_all_products_by_brandid(brand_id):
        if brand_id:
            return Product.objects.filter(brand=brand_id)
        else:
            return Product.get_all_products()
