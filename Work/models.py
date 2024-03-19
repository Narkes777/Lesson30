from dataclasses import dataclass
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Order(models.Model):
    user = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    price = models.IntegerField()

class Log(models.Model):
    text = models.TextField()
