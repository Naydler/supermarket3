
from .models import Supplier
from .serializers import SupplierSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

class SupplierListCreateView(generics.ListCreateAPIView):
    queryset= Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


#api para buscar un proveedor por nombre

@api_view(['GET'])
def search_suppliers_by_name(request):
    # Obtener el parámetro de búsqueda desde la URL (query string),request es un objeto para manejar views
    nameSupplier = request.query_params.get('name',None)
    if nameSupplier:
        # Filtrar proveedores que contengan el nombre (ignorar mayúsculas)
        suppliers = Supplier.objects.filter(name__icontains=nameSupplier)
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)
    else:
        # Si no se envía el parámetro 'name', devolver un error
        return Response({"error": "Se debe proporcionar un parámetro de búsqueda 'name'."}, status=400)
    
@api_view(['GET'])
def search_suppiers_by_nif(request):
    nifSupplier = request.query_params.get('nif',None)
    if nifSupplier:
        suppliers= Supplier.objects.filter(nif__icontains=nifSupplier)
        serializer= SupplierSerializer(suppliers,many=True)
        return Response(serializer.data)
    else:
        return Response({"error": "se debe proporcionar un parámetro de búsqueda 'nif'."},status=400)



    

    


