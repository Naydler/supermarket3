from django.http import HttpResponse, JsonResponse
from rest_framework import generics

from .serializers import CashClosingSerializer
from .serializers import CashClosing

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

class CashClosingListCreateView(generics.ListCreateAPIView):
    queryset = CashClosing.objects.all()
    serializer_class = CashClosingSerializer

class CashClosingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CashClosing.objects.all()
    serializer_class = CashClosingSerializer

