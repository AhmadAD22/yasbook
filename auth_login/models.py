from django.db import models
from django.contrib.auth.models import AbstractUser
from categroy.models import *
from django.contrib.auth.hashers import make_password

# from provider_details.models import Store


class MyUser(AbstractUser):
    last_name = None
    first_name = None
    name = models.CharField(max_length=255, blank=False, verbose_name='الاسم الكامل')
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='البريد الإلكتروني',)
    phone = models.CharField(max_length=9, verbose_name='رقم الهاتف',)
    is_active=models.BooleanField(default=True,blank=True,verbose_name='نشاط الحساب')
    is_staff=models.BooleanField(default=False,blank=True,verbose_name='دخول لوحة التحكم')
    is_superuser=models.BooleanField(default=False,blank=True,verbose_name='سوبر أدمن')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء',blank=True,null=True)
    updated_on = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث',blank=True,null=True)


class Customer(MyUser):
    latitude = models.CharField(max_length=255, verbose_name='Latitude', null=True, blank=True)
    longitude = models.CharField(max_length=255, verbose_name='Longitude', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Address', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Provider(MyUser):
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    latitude = models.CharField(max_length=255, verbose_name='Latitude', null=True, blank=True)
    longitude = models.CharField(max_length=255, verbose_name='Longitude', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Address', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Service Provider'
        verbose_name_plural = 'Service Providers'


class AdminUser(MyUser):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Admin User'
        verbose_name_plural = 'Admin Users'