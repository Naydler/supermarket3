from django.urls import path
from .views import CompanyListCreateView, CompanyRetrieveUpdateDestroyView

urlpatterns = [
    path('create/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('update/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),
]