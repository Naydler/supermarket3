
from django.urls import path,include
from .views import (SupplierListCreateView, 
                    SupplierRetrieveUpdateDestroyView,
                    search_suppliers_by_name,
                    search_suppliers_by_nif)

urlpatterns = [
    path('create/', SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('update/<int:pk>/', SupplierRetrieveUpdateDestroyView.as_view(), name='supplier-detail'),
    path('search-by-name/', search_suppliers_by_name, name='search-suppliers-by-name'),
    path('search-by-nif/', search_suppliers_by_nif, name='search-suppliers-by-nif'),
]
