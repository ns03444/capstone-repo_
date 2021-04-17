from django.db import models

# Create your models here.
class Barron(models.Model):
    title = models.CharField(max_length=300)
    time = models.CharField(max_length=300)
    link = models.URLField()
    def __str__(self):
        return self.title

class Bloomberg(models.Model):
    title = models.CharField(max_length=300)
    time = models.CharField(max_length=300)
    link = models.URLField()
    def __str__(self):
        return self.title


class Google(models.Model):
    title = models.CharField(max_length=300)
    time = models.CharField(max_length=300)
    link = models.URLField()
    def __str__(self):
        return self.title
