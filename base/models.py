from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class fashion(models.Model):
    type=models.CharField(max_length=30)
    gender=models.CharField(max_length=6,default="unisex")
    place=ArrayField(models.CharField(max_length=20))
    shirt_color=models.CharField(max_length=20)
    shirt_type=models.CharField(max_length=20)
    pant_color=models.CharField(max_length=20)
    pant_type=models.CharField(max_length=20)
    accessories=ArrayField(models.CharField(max_length=20))
    score=models.FloatField(default=1.0)