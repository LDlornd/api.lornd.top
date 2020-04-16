from django.db import models

# Create your models here.


class User(models.Model):
    openid = models.CharField(max_length=100)
    session_key = models.CharField(max_length=100)
    session = models.CharField(max_length=100, blank = True, null = True)
    province = models.CharField(max_length=100, blank = True, null = True)
    city = models.CharField(max_length=100, blank = True, null = True)
    name = models.CharField(max_length=100, blank = True, null = True)
