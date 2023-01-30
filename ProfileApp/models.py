from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=200, default='')

    def __str__(self):
        return str(self.id) + " : " + self.name + " : " + self.desc


class Product(models.Model):
    pid = models.CharField(max_length=13, primary_key=True, default='')
    name = models.CharField(max_length=50, default='')
    brand = models.CharField(max_length=30, default='')
    price = models.FloatField(default=0.00)
    net = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.pid + " : " + self.name + " : " + self.brand + " : " + self.price + " : " + self.net + " : " + self.category.name + " : "

