from django.db import models

class Productlab11:
    def __init__(self,pid, pname,brand, price, amount, promotion):
        self.__pid = pid
        self.__pname = pname
        self.__brand = brand
        self.__price = price
        self.__amount = amount
        self.__promotion = promotion
        self.__setsum()
        self.__setdiscount()
        self.__setnet()

    def __setsum(self):
        self.__sum = self.__price * self.__amount
    def __setdiscount(self):
        if self.__promotion == 'มี':
            self.__discount = self.__sum * 0.15
        else:
            self.__discount = 0.0
    def __setnet(self):
        self.__net = self.__sum - self.__discount
    def getPid(self):
        return self.__pid

    def getPname(self):
        return self.__pname

    def getBrand(self):
        return self.__brand

    def getPrice(self):
        return self.__price

    def getAmount(self):
        return self.__amount

    def getPromotion(self):
        return self.__promotion

    def getDiscount(self):
        return self.__discount

    def getNet(self):
        return self.__net

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
        return self.pid + " : " + self.name + " : " + self.brand + " : " + str(self.price) + " : " + str(self.net) + " : " + self.category.name

