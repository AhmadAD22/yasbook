from django.db import models
from auth_login.models import MyUser
# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    item_id=models.IntegerField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)