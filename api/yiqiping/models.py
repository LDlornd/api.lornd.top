from django.db import models

# Create your models here.


class User(models.Model):
    openid = models.CharField(max_length=100)
    session_key = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
