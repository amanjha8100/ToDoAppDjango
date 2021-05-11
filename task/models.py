from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
# Create your models here.
class toDo(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    