from rest_framework import generics
from .models import IvaCategory
from .serializers import IvaCategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
class IvaCategoryListCreateView(generics.ListCreateAPIView):
    queryset = IvaCategory.objects.all()
    serializer_class = IvaCategorySerializer

class IvaCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IvaCategory.objects.all()
    serializer_class = IvaCategorySerializer


@api_view(['GET'])
def get_all_ivacategory(request):
    iva_category_list = IvaCategory.objects.all()
    serializer = IvaCategorySerializer(iva_category_list, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_ivacategory_by_id(request, ivacategoryid):
    iva_category = IvaCategory.objects.filter(id=ivacategoryid)
    
    if iva_category.count() == 1:
        serializer = IvaCategorySerializer(iva_category.first())
    else:
        serializer = IvaCategorySerializer(iva_category, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_ivacategory_by_name(request, ivacategoryname):
    iva_category = IvaCategory.objects.filter(name=ivacategoryname)
    
    if iva_category.count() == 1:
        serializer = IvaCategorySerializer(iva_category.first())
    else:
        serializer = IvaCategorySerializer(iva_category, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_ivacategory_by_percentage(request, ivacategorypercentage):
    iva_category = IvaCategory.objects.filter(percentage=ivacategorypercentage)
    
    if iva_category.count() == 1:
        serializer = IvaCategorySerializer(iva_category.first())
    else:
        serializer = IvaCategorySerializer(iva_category, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_ivacategory_by_percentage_greater_than(request, ivacategorypercentage):
    iva_category = IvaCategory.objects.filter(percentage__gt=ivacategorypercentage)
    
    if iva_category.count() == 1:
        serializer = IvaCategorySerializer(iva_category.first())
    else:
        serializer = IvaCategorySerializer(iva_category, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def get_ivacategory_by_percentage_less_than(request, ivacategorypercentage):
    iva_category = IvaCategory.objects.filter(percentage__lt=ivacategorypercentage)
    
    if iva_category.count() == 1:
        serializer = IvaCategorySerializer(iva_category.first())
    else:
        serializer = IvaCategorySerializer(iva_category, many=True)
    
    return Response(serializer.data)


