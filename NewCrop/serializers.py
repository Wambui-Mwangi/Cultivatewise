from rest_framework import serializers
from .models import AddedCrop

class UserCropSerializer(serializers.ModelSerializer):
    class meta:
        model = AddedCrop
        fields = '__all__'