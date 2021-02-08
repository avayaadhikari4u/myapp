from django.db import models
from .product import Product
from .customer import Customer
import datetime
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    date=models.DateField(default=datetime.datetime.today)
    
    def __str__(self):
        return self.product
    '''
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Orders\
        .objects\
        .filter(customer=customer_id)\
        .order_by('-date')
    '''