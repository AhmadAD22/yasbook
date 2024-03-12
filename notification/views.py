from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from channels.layers import get_channel_layer
from channels_redis.core import RedisChannelLayer

from asgiref.sync import async_to_sync
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')


class NotificationAPIView(APIView):
    def post(self, request):
        recipient = request.user  # Assuming you are using authentication
        message = request.data.get('message')
        notification = Notification.objects.create(recipient=recipient, message=message,item_id=1,type="test")

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'user_8',
            {
                'type': 'send_notification',
                'notification': {
                    'id': notification.id,
                    'message': notification.message,
                    'timestamp': notification.timestamp.strftime('%Y-%m-%d %H:%M:%S')
                }
            }
        )

        return Response({'status': 'success'})

    def get(self, request):
        recipient = request.user
        notifications = Notification.objects.filter(recipient=recipient)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)