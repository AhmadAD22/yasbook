from django.db import models

# Create your models here.
class Term (models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()

class Privacy(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
        