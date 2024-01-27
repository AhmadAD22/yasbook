from django.db import models
from provider_details.models import *
from auth_login.models import *

class ProductOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    accept = models.BooleanField(default=False, verbose_name='موافقة التاجر',null=True,blank=True)

    def __str__(self):   
        return self.product.name
    
class ServiceOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    specialist = models.ForeignKey(StoreSpecialist, on_delete=models.CASCADE,null=True)
    time_start=models.TimeField(verbose_name='وقت البدء' ,null=True)
    date = models.DateTimeField( verbose_name='تاريخ الحجز',blank=True,null=True)
    duration = models.TimeField( verbose_name='مدة الخدمة',blank=True,null=True)
    accept = models.BooleanField(default=False, verbose_name='موافقة التاجر',null=True,blank=True)

    def __str__(self):   
        return self.service.name