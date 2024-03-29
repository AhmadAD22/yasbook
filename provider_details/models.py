from django.db import models
from auth_login.models import *
from categroy.models import MainService
import os
from django.core.validators import MinValueValidator, MaxValueValidator


class Store(models.Model):
    provider = models.OneToOneField(Provider, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/provider/store/',null=True,blank=True, verbose_name='رفع الصورة')
    name = models.CharField(max_length=255, verbose_name='اسم المتجر',null=True,blank=True,)
    about = models.TextField(blank=True, null=True, verbose_name='الوصف')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء',blank=True,null=True)
    updated_on = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث',blank=True,null=True)
    
    def delete(self, *args, **kwargs):
        # Delete the associated image file
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        
        super(Store, self).delete(*args, **kwargs)


class StoreAdminServices(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    main_service = models.ForeignKey(MainService, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Services for Store"

class StoreSpecialist(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='اسم الموظف',)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء',blank=True,null=True)
    updated_on = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث',blank=True,null=True)

class StoreOpening(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    day = models.CharField(max_length=255, verbose_name='اليوم',)
    time_start=models.TimeField(verbose_name='وقت البدء')
    time_end=models.TimeField(verbose_name='وقت الانتهاء')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء',blank=True,null=True)
    updated_on = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث',blank=True,null=True)

class FollowingStore(models.Model):
    store = models.ForeignKey(Store, verbose_name='المتجر التابع له', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name='الزبون', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['store', 'customer']

class StoreStory(models.Model):
    store = models.ForeignKey(Store, verbose_name='المتجر التابع له',related_name='story_of_store', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/provider/store/',null=True,blank=True, verbose_name='رفع الصورة')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء',blank=True,null=True)


    class Meta:
        unique_together = ['store', 'image']

class StoreGallery(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/provider/gallery/', verbose_name='رفع الصورة')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء',blank=True,null=True)
    updated_on = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث',blank=True,null=True)

    def delete(self, *args, **kwargs):
        # Delete the associated image file
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        
        super(StoreGallery, self).delete(*args, **kwargs)


class Service(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    main_service = models.ForeignKey(MainService, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='media/provider/service/', verbose_name='رفع الصورة')
    name = models.CharField(max_length=255, verbose_name='اسم الخدمة')
    description = models.TextField(blank=True, null=True, verbose_name='الوصف')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر',null=True)
    offers = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0,blank=False, verbose_name='الخصم')
    hours_Service = models.TextField(blank=True, null=True, verbose_name='ساعات الخدمة')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء',blank=True,null=True)
    updated_on = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث',blank=True,null=True)


    def delete(self, *args, **kwargs):
        # Delete the associated image file
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        
        super(StoreGallery, self).delete(*args, **kwargs)

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/provider/service/', verbose_name='رفع الصورة')
    name = models.CharField(max_length=255, verbose_name='اسم المنتج')
    description = models.TextField(blank=True, null=True, verbose_name='الوصف')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='السعر')
    offers = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0,blank=False, verbose_name='الخصم')
    hours_Service = models.TimeField(blank=True, null=True, verbose_name='ساعات الخدمة')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء',blank=True,null=True)
    updated_on = models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث',blank=True,null=True)


    def delete(self, *args, **kwargs):
        # Delete the associated image file
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        
        super(StoreGallery, self).delete(*args, **kwargs)


class Reviews(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True,verbose_name='الزبون')
    store = models.ForeignKey(Store, on_delete=models.CASCADE,verbose_name='المتجر')
    message = models.TextField(verbose_name='رسالة')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True, verbose_name='تقييم المنتج')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء',blank=True,null=True)


    def __str__(self):
        return f"Message by {self.customer.username} "