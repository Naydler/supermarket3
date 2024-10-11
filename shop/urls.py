from django.urls import path
from .views import ShopListCreateView, ShopRetrieveUpdateDestroyView

urlpatterns = [
    path('create/', ShopListCreateView.as_view(), name='shop-list-create'),
    path('update/<int:pk>/', ShopRetrieveUpdateDestroyView.as_view(), name='`shop`-detail'),
]