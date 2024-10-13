from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView
from .views import *

urlpatterns = [
    path('create/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('update/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='`employee`-detail'),



    path('api/byshop/<int:shopid>/', get_employees_by_shopid, name='employee-by-shopid'),
    path('api/bycompany/<int:companyid>/', get_all_employees_by_company, name='employee-by-company'),

]