
from .models import Supplier
from .serializers import SupplierSerializer
from rest_framework import generics


# Create your views here.

class SupplierListCreateView(generics.ListCreateAPIView):
    queryset= Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
