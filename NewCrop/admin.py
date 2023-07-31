from django.contrib import admin
from .models import AddedCrop

# Register your models here.
class AddedCropAdmin(admin.ModelAdmin):
    list_display = ('user', 'crop', 'crop_name', 'crop_category', 'description', 'ideal_climate', 'water_requirements', 'soil_type', 'growth_duration')

admin.site.register(AddedCrop, AddedCropAdmin)