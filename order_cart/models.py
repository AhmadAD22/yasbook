from django.db import models
from provider_details.models import *
from auth_login.models import *


class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    @property
    def total_price(self):
        product_items = self.cartitem_set.all()
        service_items = self.servicecartitem_set.all()

        product_total = sum(item.product.price * item.quantity for item in product_items)
        service_total = sum(item.service.price * item.quantity for item in service_items)

        return product_total + service_total
    def __str__(self):   
        return self.customer.name

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class ServiceCartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    specialist = models.ForeignKey(StoreSpecialist, on_delete=models.CASCADE, null=True)
    time_start = models.TimeField(verbose_name='وقت البدء', null=True)
    date = models.DateTimeField(verbose_name='تاريخ الحجز', blank=True, null=True)
    duration= models.PositiveIntegerField(verbose_name='مدة الخدمة (بالدقائق)', blank=True, null=True)


    class Meta:
        verbose_name = 'Service Cart Item'
        verbose_name_plural = 'Service Cart Items'


class ProductOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    accept = models.BooleanField(default=False, verbose_name='موافقة التاجر',null=True,blank=True)
    collected = models.BooleanField(default=False, verbose_name='تم تحصيلها', null=True, blank=True)
    date= models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء',blank=True,null=True)




    def __str__(self):   
        return self.product.name
    
class ServiceOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    specialist = models.ForeignKey(StoreSpecialist, on_delete=models.CASCADE,null=True)
    time_start=models.TimeField(verbose_name='وقت البدء' ,null=True)
    date = models.DateTimeField( verbose_name='تاريخ الحجز',blank=True,null=True)
    duration= models.PositiveIntegerField(verbose_name='مدة الخدمة (بالدقائق)', blank=True, null=True)
    accept = models.BooleanField(default=False, verbose_name='موافقة التاجر',null=True,blank=True)
    collected = models.BooleanField(default=False, verbose_name='تم تحصيلها', null=True, blank=True)
    
    

    def __str__(self):   
        return self.service.name