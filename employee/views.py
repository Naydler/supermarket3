from rest_framework import generics
from .models import Employee
from .serializers import CompanySerializer

# Create your views here.

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = CompanySerializer

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = CompanySerializer