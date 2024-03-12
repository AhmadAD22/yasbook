from django.db import models
from django.contrib.auth.models import AbstractUser
from categroy.models import *
from django.contrib.auth.hashers import make_password
from datetime import datetime, timezone,date


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
        
        


from datetime import datetime, timedelta

from django.db import models
from datetime import timedelta, datetime
from provider_details.models import Provider

class ProviderSubscription(models.Model):
    DURATION_CHOICES = (
        (90, '90 days'),
        (180, '180 days'),
        (365, '365 days'),
    )

    provider = models.OneToOneField(Provider, verbose_name="provider", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Subscription date")
    duration_days = models.IntegerField(choices=DURATION_CHOICES, verbose_name="Duration")
    service_profit = models.IntegerField(default=0, blank=False, verbose_name='service profit')
    store_subscription = models.BooleanField(verbose_name='Store subscription', default=False)
    product_profit = models.IntegerField(default=0, blank=True, verbose_name='product profit')

    @property
    def duration(self):
        return timedelta(days=self.duration_days)

    def remaining_duration(self):
        current_date = datetime.now().date()
        subscription_end_date = self.date + self.duration
        remaining_days = (subscription_end_date - current_date).days
        return max(remaining_days, 0)

    def is_duration_finished(self):
        current_date = datetime.now().date()
        end_date = self.date + self.duration
        return current_date > end_date
    
    
    def __str__(self):
        return self.provider.name + " Remaining:  "+str(self.remaining_duration())+ " Days, Finished: " + str(self.is_duration_finished())
    


class PromotionSubscription(models.Model):
    DURATION_CHOICES = (
        (3, '3 days'),
        (7, '7 days'),
        (15, '15 days'),
        (30, '30 days'),
        (45, '45 days'),
        
    )
    
    provider = models.OneToOneField(Provider, verbose_name="provider", on_delete=models.CASCADE)
    promotion_date = models.DateField(blank=True, null=True, verbose_name="Promotion start date")
    promotion_duration_days = models.IntegerField(choices=DURATION_CHOICES, verbose_name="Promotion Duration", blank=True, null=True)
    profit = models.IntegerField(default=0, blank=True, verbose_name='product profit')

    @property
    def promotion_duration(self):
        if self.promotion_duration_days:
            return timedelta(days=self.promotion_duration_days)
        return None

    def remaining_duration(self):
        if self.promotion_date and self.promotion_duration:
            current_date = date.today()
            promotion_end_date = self.promotion_date + self.promotion_duration
            remaining_days = (promotion_end_date - current_date).days
            return max(remaining_days, 0)
        return None

    def is_duration_finished(self):
        remaining_duration = self.remaining_duration()
        return remaining_duration == 0
    def __str__(self):
        return self.provider.name + " Remaining:  "+str(self.remaining_duration())+ " Days, Finished: " + str(self.is_duration_finished())