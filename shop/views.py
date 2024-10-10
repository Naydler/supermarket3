from rest_framework import generics
from .models import Shop
from .serializers import CompanySerializer

# Create your views here.

class ShopListCreateView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = CompanySerializer

class ShopRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = CompanySerializer