from django.db import models

# Create your models here.

class Store(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image/")
    address = models.CharField(max_length=200)
    menu_title = models.CharField(max_length=200)
    menu_image = models.ImageField(upload_to="image/")
    
    def __str__(self):
        return self.title

class Order(models.Model):

    CHOICES = (
        ('배민', '배민페이'),
        ('신용', '신용카드'),
        ('계좌', '계좌이체'),
        ('무통장', '무통장입금')
    )

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=100)
    pay = models.CharField(max_length=200, choices = CHOICES )

    def __str__(self):
        return self.name