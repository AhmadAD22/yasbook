from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
import json
from provider_details.models import FollowingStore
from auth_login.models import *
from asgiref.sync import sync_to_async


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        try:
            token_name, token_key = self.scope['query_string'].decode().split('=')
            if token_name == 'token':
                user = await self.get_user_from_token(token_key)
                if user is None:
                    raise AuthenticationFailed('Invalid token')
                self.user = user
            else:
                raise AuthenticationFailed('Token not provided')
        except (ValueError, AuthenticationFailed) as e:
            await self.close(code=1002)  # Close the connection with 1002 code (Protocol Error)
            return
        self.group_name = "user_"+user.id
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def send_notification(self, event):
        await self.send(text_data=json.dumps(event['notification']))

    @database_sync_to_async
    def get_user_from_token(self, token_key):
        try:
            token = Token.objects.select_related('user').get(key=token_key)
            return token.user
        except Token.DoesNotExist:
            return None
        
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync

class Customer2NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        try:
            token_name, token_key = self.scope['query_string'].decode().split('=')
            if token_name == 'token':
                user = await self.get_user_from_token(token_key)
                if user is None:
                    raise AuthenticationFailed('Invalid token')
                self.user = user
            else:
                raise AuthenticationFailed('Token not provided')
        except (ValueError, AuthenticationFailed) as e:
            await self.close(code=1002)  # Close the connection with 1002 code (Protocol Error)
            return
        user_group='user_'+str(user.id)
        print(user_group)
        await self.channel_layer.group_add(
                str(user_group),
                self.channel_name
            )
        # Add the user to the stores they follow
        following_stores = await self.get_following_stores(user)
        self.group_names = [store.store.id for store in following_stores]

        for group_name in self.group_names:
            group_name="store_"+str(group_name)
            print(group_name)
            await self.channel_layer.group_add(
                str(group_name),
                self.channel_name
            )

    async def disconnect(self, close_code):
        for group_name in self.group_names:
            group_name="stor_"+str(group_name)
            await self.channel_layer.group_discard(
                group_name,
                self.channel_name
            )

    async def send_notification(self, event):
        await self.send(text_data=json.dumps(event['notification']))

    @database_sync_to_async
    def get_user_from_token(self, token_key):
        try:
            token = Token.objects.select_related('user').get(key=token_key)
            return token.user
        except Token.DoesNotExist:
            return None

    @sync_to_async
    def get_following_stores(self, user):
        following_stores = FollowingStore.objects.filter(customer=user)
        print(following_stores)
        following_stores = list(following_stores.select_related('store'))
        print(following_stores)
        return following_stores