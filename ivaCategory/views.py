from rest_framework import generics
from .models import IvaCategory
from .serializers import IvaCategorySerializer

# Create your views here.
class IvaCategoryListCreateView(generics.ListCreateAPIView):
    queryset = IvaCategory.objects.all()
    serializer_class = IvaCategorySerializer

class IvaCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IvaCategory.objects.all()
    serializer_class = IvaCategorySerializer