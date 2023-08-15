from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu, Booking
from . serializers import MenuSerializer, BookingSerializer
from rest_framework import serializers, permissions
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingView(generics.ListCreateAPIView):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   permission_classes = [permissions.IsAuthenticated] 

