from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Qr_code(models.Model):
    user = models.ForeignKey(to= User, on_delete=models.CASCADE, null= True)
    link = models.CharField(max_length= 255)
    color = models.CharField(max_length= 7, default='#000000')
    size = models.IntegerField()