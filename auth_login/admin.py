from django.contrib import admin

from .models import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Provider, AdminUser
from django.urls import reverse
from django.utils.html import format_html
from provider_details.models import Store


class CustomerAdmin(UserAdmin):
    list_display = ('name','username', 'phone', 'address')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('name', 'phone', 'address')
    readonly_fields = ('latitude','longitude')
    fieldsets = (
        (None, {'fields': ('name', 'password')}),
        ('Permissions', {'fields': ('is_active',)}),
        ('Contact Information', {'fields': ('phone', 'address')}),
        ('Location', {'fields': ('latitude', 'longitude')}),
    )

admin.site.register(Customer, CustomerAdmin)


class ProviderAdmin(UserAdmin):
    list_display = ('name', 'category', 'phone', 'address')
    list_filter = ('is_active', 'is_staff', 'category')
    search_fields = ('name', 'phone', 'address')
    readonly_fields = ('latitude','longitude','store_name')

    fieldsets = (
        (None, {'fields': ('name', 'password')}),
        ('Permissions', {'fields': ('is_active',)}),
        ('Contact Information', {'fields': ('phone', 'address')}),
        ('Location', {'fields': ('latitude', 'longitude')}),
        ('Category', {'fields': ('category',)}),
        ('Store', {'fields': ('store_name',)}),
    )
    def store_name(self, obj):
        if obj:
            store=Store.objects.get(provider=obj.id)
            store_url = reverse('admin:provider_details_store_change', args=[store.id])
            return format_html('<a href="{}">{}</a>', store_url, store.name)
        return "N/A"
    store_name.short_description = 'Store Name'

    def store_link(self, obj):
        if obj:
            store=Store.objects.get(provider=obj.id)
            store_url = reverse('admin:provider_details_store_change', args=[store.id])
            return format_html('<a href="{}">{}</a>', store_url, store.name)
        return "N/A"
    store_link.short_description = 'Store Link'
admin.site.register(Provider, ProviderAdmin)


class AdminUserAdmin(UserAdmin):
    list_display = ('name', 'phone', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('name', 'phone')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Contact Information', {'fields': ('name','phone','email')}),
    )
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(AdminUser, AdminUserAdmin)

from django.contrib import admin
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html

class ProviderSubscriptionAdmin(admin.ModelAdmin):
    readonly_fields = ('details',)

    def details(self, obj):
        return format_html('<a href="http://127.0.0.1:8000/">Clic to show more details</a>') 
    details.short_description = 'Details'

admin.site.register(ProviderSubscription, ProviderSubscriptionAdmin)
admin.site.register(PromotionSubscription)