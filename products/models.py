from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    x=[('Phone', 'Phone'), ("Computer", "Computer")]
    name= models.CharField(max_length=100 , default='name' , verbose_name='Title')
    content= models.TextField(blank=True , verbose_name='Description' )
    price= models.DecimalField(max_digits=5 , decimal_places=2 , null=True)
    image= models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)
    category= models.CharField(max_length=50 , null=True , blank=True , choices=x)
    def __str__(self):
        return self.name
    class Meta :
        verbose_name='name'
        ordering=['-price']

class Test(models.Model):
    date=models.DateField()
    time= models.TimeField(null=True)
    created = models.DateTimeField(default=datetime.now)