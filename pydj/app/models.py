from django.db import models

# Create your models here.
class Category(models.Model):
    code = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True) #mo ta
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT) # khi con sp thi k cho xoa
    image = models.ImageField(upload_to='static/images')
    def __str__(self):
        return self.name
