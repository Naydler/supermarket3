from rest_framework import serializers

from supplier.models import Supplier
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    id_supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    supplier_name = serializers.CharField(source='id_supplier.name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
