from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('create/', ProductListCreateView.as_view(), name='product-list-create'),
    path('update/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='`product`-detail'),
]