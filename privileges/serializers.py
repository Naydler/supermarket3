from rest_framework import serializers
from .models import Privilege

class PrivilegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privilege
        fields = '__all__'  # O especifica los campos que quieres incluir