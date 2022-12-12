from django.db import models
from datetime import datetime

# Create your models here 

class People(models.Model):

    name = models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    batch=models.CharField(max_length=100)
    date=models.DateField(default=datetime.now())
    fees = models.BooleanField(default=False )
    batch_date= models.DateField(default=datetime.now())

    def __str__(self):
       return self.name
    
