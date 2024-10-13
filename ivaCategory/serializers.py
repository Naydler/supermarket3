from rest_framework import serializers
from .models import IvaCategory

class IvaCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IvaCategory
        fields = '__all__'