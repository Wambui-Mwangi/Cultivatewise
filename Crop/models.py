from django.db import models

# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField()
    ideal_climate = models.CharField(max_length=50)
    water_requirements = models.CharField(max_length=50)
    soil_type = models.CharField(max_length=50)
    growth_duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name
