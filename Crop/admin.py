from django.contrib import admin
from .models import Plant

# Register your models here.
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'image', 'ideal_climate', 'water_requirements', 'soil_type', 'growth_duration')

admin.site.register(Plant, PlantAdmin)
