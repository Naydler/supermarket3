from django.urls import path
from .views import *


urlpatterns = [
    path('create/', OfferListCreateView.as_view(), name='offer-list-create'),
    path('update/<int:pk>/', OfferRetrieveUpdateDestroyView.as_view(), name='offer-detail'),

    path('api/byshop/<int:shopid>/', get_offers_by_shopid, name='offer-by-shopid'),
    path('api/byemployee/<int:employeeid>/', get_offer_by_employee, name='offer-by-employee'),

]