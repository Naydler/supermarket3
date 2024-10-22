from django.urls import path
from .views import ClientListCreateView, ClientRetrieveUpdateDestroyView

urlpatterns = [
    path('create/', ClientListCreateView.as_view(), name='client-list-create'),
    path('update/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),
]