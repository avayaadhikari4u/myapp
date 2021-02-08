from django.db import models
from .product import Product
from .customer import Customer
import datetime
class Orders(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=50,default='',blank=True)
    phone=models.CharField(max_length=15,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    Pending=models.BooleanField(default=True)
    OnTheWay=models.BooleanField(default=False)
    Completed=models.BooleanField(default=False)

    def __str__(self):
        return self.customer.first_name +" "+ self.customer.last_name

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Orders\
        .objects\
        .filter(customer=customer_id)\
        .order_by('-date')