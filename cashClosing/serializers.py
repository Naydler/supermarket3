from rest_framework import serializers
from .models import CashClosing

class CashClosingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashClosing
        fields = '__all__'