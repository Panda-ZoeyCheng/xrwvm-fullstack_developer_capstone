from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    origin_country = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.TextField()
    name = models.CharField(max_length=250)
    type = models.CharField(
        max_length=10,
        choices=[
            ('SEDAN', 'Sedan'),
            ('SUV', 'SUV'),
            ('WAGON', 'Wagon')
        ]
    )
    year = models.IntegerField(
        default=2023,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )

    def __str__(self):
        return self.name
