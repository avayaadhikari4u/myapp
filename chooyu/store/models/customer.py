from django.db import models

class Customer(models.Model):
    first_name= models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    confirm_password=models.CharField(max_length=500)
    image=models.ImageField(upload_to='uploads/customer/',default='',blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def register(self):
        self.save()

    @staticmethod
    def get_user(email):
        try:
            print(email)
            return Customer.objects.get(email=email)

        except:
            return False
    
    
    @staticmethod
    def get_customers_by_id(ids):
        return Customer.objects.filter(id__in=ids)


    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    def get_all_customer():
        return Customer.objects.all()

    @staticmethod
    def get_customer_by_id(ids):
        return Customer.objects.filter(id__in=ids)