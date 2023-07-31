from django.db import models
from Crop.models import Plant
from User.models import Customer
from NewCrop.models import AddedCrop

# Create your models here.
class Review(models.Model):
     user = models.ForeignKey(Customer, on_delete=models.CASCADE)
     crop = models.ForeignKey(Plant, on_delete=models.CASCADE)
     new_crop = models.ForeignKey(AddedCrop, on_delete=models.CASCADE)
     comment = models.TextField()

     def __str__(self):
          return self.crop
