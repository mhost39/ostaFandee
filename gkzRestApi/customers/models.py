from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    phone = models.CharField(default=False,max_length=11)
    passwod = models.CharField(default=False,max_length=50)