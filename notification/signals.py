from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notification
from provider_details.models import *
from order_cart.models import *
# Customer folloings notifications
@receiver(post_save, sender=FollowingStore)
def notification_created(sender, instance, created, **kwargs):
    if created:
        message=str(instance.customer) +' liked your store'
        notification = Notification.objects.create(recipient=instance.store.provider, message=message,type="customer_like",item_id=instance.customer.id)
        group_name='user_'+str(instance.store.provider.id)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            str(group_name),
            {
                'type': 'send_notification',
                'notification': {
                    'id': notification.id,
                    'message': message,
                    'timestamp': notification.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    'type':notification.type,
                    'item_id':notification.item_id
                }
            }
        )
#Add new Product notifications
@receiver(post_save, sender=Product)
def notification_created(sender, instance, created, **kwargs):
    if created:
        #Notification
        #Add store name to notification massege
        message = str(instance.store.name) +" has added a new product"
        # Get all folloers to store that added product
        followers=FollowingStore.objects.filter(store=instance.store)
        for follower in followers:
            #Make notification per follower
            notification = Notification.objects.create(recipient=follower.customer, message=message,type="add_product",item_id=instance.id)
        group_name='store_'+str(instance.store.id)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            str(group_name),
            {
                'type': 'send_notification',
                'notification': {
                    'id': "",
                    'message': message,
                    'timestamp': "",
                    'type':"add_product",
                    'item_id': instance.id
                    
                }
            }
        )
        
#Add new Service notifications
@receiver(post_save, sender=Service)
def notification_created(sender, instance, created, **kwargs):
    if created:
        #Notification
        #Add store name to notification massege
        message = str(instance.store.name) +" has added a new srvice"
        # Get all folloers to store that added Service
        followers=FollowingStore.objects.filter(store=instance.store)
        for follower in followers:
            #Make notification per follower
            notification = Notification.objects.create(recipient=follower.customer, message=message,type="add_service",item_id=instance.id)
        group_name='store_'+str(instance.store.id)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            str(group_name),
            {
                'type': 'send_notification',
                'notification': {
                    'id': "",
                    'message': message,
                    'timestamp': "",
                    'type':"add_service",
                    'item_id': instance.id
                    
                }
            }
        )
        # Service orders notifications
@receiver(post_save, sender=ServiceOrder)
def notification_created(sender, instance, created, **kwargs):
    if created:
        message=str(instance.customer) +' has requsted to book the service: '+str(instance.service.name)
        print(message)
        notification = Notification.objects.create(recipient=instance.service.store.provider, message=message,type="customer_service_order",item_id=instance.id)
        group_name='user_'+str(instance.service.store.provider.id)
        print(group_name)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            str(group_name),
            {
                'type': 'send_notification',
                'notification': {
                    'id': notification.id,
                    'message': message,
                    'timestamp': notification.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    'type':notification.type,
                    'item_id':notification.item_id
                }
            }
        )
        
        
        # Product orders notifications
@receiver(post_save, sender=ProductOrder)
def notification_created(sender, instance, created, **kwargs):
    if created:
        message=str(instance.customer) +' has requsted to book the product: '+str(instance.product.name)
        notification = Notification.objects.create(recipient=instance.product.store.provider, message=message,type="customer_service_order",item_id=instance.id)
        group_name='user_'+str(instance.product.store.provider.id)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            str(group_name),
            {
                'type': 'send_notification',
                'notification': {
                    'id': notification.id,
                    'message': message,
                    'timestamp': notification.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    'type':notification.type,
                    'item_id':notification.item_id
                }
            }
        )