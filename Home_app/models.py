from django.db import models

# Create your models here.


class StockModel(models.Model):
    stockname=models.CharField(max_length=100)
    high=models.FloatField()
    low=models.FloatField()
    value=models.FloatField()
    stockdetail=models.TextField(null=True)
    slug=models.SlugField(unique=True)


    
    def __str__(self):
        return self.stockname