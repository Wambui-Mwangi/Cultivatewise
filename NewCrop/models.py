from django.db import models
from User.models import Customer
from Crop.models import Plant

# Create your models here.
class AddedCrop(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    crop = models.ForeignKey(Plant, on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=30)
    description = models.TextField()
    ideal_climate = models.CharField(max_length=100)
    water_requirements = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=100)
    growth_duration = models.CharField(max_length=100)

    def __str__(self):
        return self.crop_name


