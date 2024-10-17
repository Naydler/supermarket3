from django.urls import path
from .views import *

urlpatterns = [
    path('create/', IvaCategoryListCreateView.as_view(), name='ivaCategory-list-create'),
    path('update/<int:pk>/', IvaCategoryRetrieveUpdateDestroyView.as_view(), name='`ivaCategory`-detail'),

    path('api/getallivacategory/', get_all_ivacategory, name='`ivaCategory`-list'),
    path('api/getivacategorybyid/<int:ivacategoryid>/', get_ivacategory_by_id, name='`ivaCategory`-detail'),
    path('api/getivacategorybyname/<str:ivacategoryname>/', get_ivacategory_by_name, name='`ivaCategory`-detail'),
    path('api/getivacategorybypercentage/<str:ivacategorypercentage>/', get_ivacategory_by_percentage, name='`ivaCategory`-detail'),
    path('api/getivacategorybypercentagegreaterthan/<str:ivacategorypercentage>/', get_ivacategory_by_percentage_greater_than, name='`ivaCategory`-detail'),
    path('api/getivacategorybypercentagelessthan/<str:ivacategorypercentage>/', get_ivacategory_by_percentage_less_than, name='`ivaCategory`-detail'),
    

]