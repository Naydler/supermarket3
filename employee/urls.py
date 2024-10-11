from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView

urlpatterns = [
    path('create/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('update/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='`employee`-detail'),
]