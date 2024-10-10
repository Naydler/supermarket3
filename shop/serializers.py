from rest_framework import serializers
from .models import Shop

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'