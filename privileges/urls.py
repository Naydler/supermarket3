from django.urls import path
from .views import PrivilegeListCreateView, PrivilegeRetrieveUpdateDestroyView

urlpatterns = [
    path('create/', PrivilegeListCreateView.as_view(), name='employee-list-create'),
    path('update/<int:pk>/', PrivilegeRetrieveUpdateDestroyView.as_view(), name='`employee`-detail'),
]