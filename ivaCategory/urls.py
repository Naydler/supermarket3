from django.urls import path
from .views import IvaCategoryListCreateView,IvaCategoryRetrieveUpdateDestroyView

urlpatterns = [
    path('create/', IvaCategoryListCreateView.as_view(), name='ivaCategory-list-create'),
    path('update/<int:pk>/', IvaCategoryRetrieveUpdateDestroyView.as_view(), name='`ivaCategory`-detail'),
]