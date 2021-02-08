from django.db import models
class Category(models.Model):

    name= models.CharField(max_length=50)
    image=models.ImageField(upload_to='uploads/catagory/')

    def __str__(self):
        return self.name


    @staticmethod

    def get_all_categories():
        return Category.objects.all()

class SubCategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    image=models.ImageField(upload_to='uploads/catagory/')

    def __str__(self):
        return self.name


    @staticmethod

    def get_all_subcategories():
        return SubCategory.objects.all()

    @staticmethod

    def get_all_subCategory_by_categoryid(category_id):
        if category_id:
            return SubCategory.objects.filter(category=category_id)
        else:
            return get_all_subcategories.objects.all()

class Brand(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    image=models.ImageField(upload_to='uploads/catagory/')

    def __str__(self):
        return self.name


    @staticmethod

    def get_all_Brand():
        return Brand.objects.all()

    @staticmethod

    def get_all_Brands_by_subcategoryid(subcategory_id):
        if subcategory_id:
            return Brand.objects.filter(subcategory=subcategory_id)
        else:
            return get_all_Brand.objects.all()