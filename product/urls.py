from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView
from .views import *

urlpatterns = [
    path('create/', ProductListCreateView.as_view(), name='product-list-create'),
    path('update/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='`product`-detail'),
    path('getallproducts/', get_all_products, name='get-all-products')
]