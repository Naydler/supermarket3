
from django.urls import path,include
from .views import SupplierListCreateView, SupplierRetrieveUpdateDestroyView

urlpatterns = [
    path('create/', SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('update/<int:pk>/', SupplierRetrieveUpdateDestroyView.as_view(), name='supplier-detail'),
]
