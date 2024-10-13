from rest_framework import generics
from .models import Privilege
from .serializers import PrivilegeSerializer

# Create your views here.

class PrivilegeListCreateView(generics.ListCreateAPIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer

class PrivilegeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer