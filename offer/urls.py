from django.urls import path
from .views import OfferListCreateView, OfferRetrieveUpdateDestroyView


urlpatterns = [
    path('create', OfferListCreateView.as_view(), name='offer-list-create'),
    path('update/<int:pk>/', OfferRetrieveUpdateDestroyView.as_view(), name='offer-detail'),
]