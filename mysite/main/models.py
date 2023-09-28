from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age  = models.IntegerField()

    address = models.TextField()

    gender_types = [
        ("F", "Female"),
        ("M", "Male")
       
    ]

    gender =  models.CharField(max_length= 5,  choices=gender_types)

class Car(models.Model):
    car_name = models.CharField( max_length= 100)
    speed = models.IntegerField(default=50)
    