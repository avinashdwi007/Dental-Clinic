from django.db import models

# Create your models here.

class data(models.Model):
    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=15)
    message=models.TextField()

    def __str__(self):
        return self.name
    