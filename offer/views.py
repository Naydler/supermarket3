from rest_framework import generics
from .models import Offer
from .serializers import OfferSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
class OfferListCreateView(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class OfferRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer



@api_view(['GET'])
def get_offers_by_shopid(request, shopid):
    offers = Offer.objects.filter(idShop_id=shopid)

    # Check if there is only one offer
    if offers.count() == 1:
        # if there is only one, use many=False
        serializer = OfferSerializer(offers.first())
    else:
        # if there is more than one, use many=True
        serializer = OfferSerializer(offers, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_offer_by_employee(request, employeeid):
    offers = Offer.objects.filter(idEmployee_id=employeeid)

    if offers.count() == 1:
        serializer = OfferSerializer(offers.first())
    else:
        serializer = OfferSerializer(offers, many=True)

    return Response(serializer.data)