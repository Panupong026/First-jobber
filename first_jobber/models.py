from django.db import models

# Create your models here.

class Insurance(models.Model):
    name = models.CharField(max_length=255)
    insurance_class = models.CharField(max_length=100)
    price = models.IntegerField()
    urls = models.TextField(default='N/A')

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Coverage(models.Model):
    insuranceId = models.ForeignKey(Insurance, on_delete=models.CASCADE, related_name='insuranceId')
    car = models.IntegerField()
    medicine = models.IntegerField()
    third_party = models.IntegerField()
    lost = models.BooleanField()
