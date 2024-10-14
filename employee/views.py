from django.http import HttpResponse, JsonResponse
from rest_framework import generics

from company.models import Company
from company.serializers import CompanySerializer
from shop.models import Shop
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@api_view(['GET'])
def get_employees_by_shopid(request, shopid):
    employees = Employee.objects.filter(shopid_id=shopid)

    # Check if there is only one employee
    if employees.count() == 1:
        # if there is only one, use many=False
        serializer = CompanySerializer(employees.first())
    else:
        # if there is more than one, use many=True
        serializer = CompanySerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_employees_by_company(request, companyid):
    # get all shops by company
    # return example: {'id': 1, 'idCompany_id': 1, 'name': 'Hypermercado'}
    shops = Shop.objects.filter(idCompany=companyid)
    

    # Filter the employees that belong to these stores
    # Example of return [ { "id": 1, "name": "Hypermercado", "idCompany": 1 } ] 
    employees = Employee.objects.filter(shopid__in=shops)
    
    # Use a CompanySerializer to Serialze a data
    serializer = CompanySerializer(employees, many=True)
    
    return Response(serializer.data)



