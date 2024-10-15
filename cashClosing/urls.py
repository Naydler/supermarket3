from django.urls import path
from .views import CashClosingListCreateView, CashClosingRetrieveUpdateDestroyView


urlpatterns = [
    path('create/', CashClosingListCreateView.as_view(), name='employee-list-create'),
    path('update/<int:pk>/', CashClosingRetrieveUpdateDestroyView.as_view(), name='`employee`-detail'),
]