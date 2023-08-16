from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class user_otp(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE)
  email = models.EmailField()
  otp = models.CharField(max_length=4)
