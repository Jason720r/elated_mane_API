"""Customer class module"""
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """Customer model class"""
    stylist = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    style = models.ForeignKey("HairStyle", on_delete=models.CASCADE)
    date_created = models.DateField(auto_now=True)
