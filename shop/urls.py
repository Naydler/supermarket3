from django.urls import path
from .views import ShopListCreateView, ShopRetrieveUpdateDestroyView

urlpatterns = [
    path('createshop/', ShopListCreateView.as_view(), name='shop-list-create'),
    path('updateshop/<int:pk>/', ShopRetrieveUpdateDestroyView.as_view(), name='`shop`-detail'),
]