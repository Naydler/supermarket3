from django.urls import path
from .views import CompanyListCreateView, CompanyRetrieveUpdateDestroyView

urlpatterns = [
    path('createcompany/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('updatecompany/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),
]