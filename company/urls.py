from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('createcompany/', ProductListCreateView.as_view(), name='product-list-create'),
    path('updatecompany/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]