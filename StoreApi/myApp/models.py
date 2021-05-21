from django.db import models

# Create your models here.
class Item(models.Model):
    item=models.CharField(max_length=100)
    itemCategory=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.IntegerField()