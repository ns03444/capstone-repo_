from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    link = models.URLField(null=True)
    def __str__(self):
        return self.ticker

# Create your models here.
