from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class extendeduser(models.Model):
    address = models.CharField(max_length = 30, default='SOME STRING')
    email = models.CharField(max_length = 30, default='SOME STRING')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
