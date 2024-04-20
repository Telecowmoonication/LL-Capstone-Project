from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class bookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)
    

## This was in the course instructions at one point but then seems to get switched out for menuitemsview
# class menuview(APIView):
#     def post(self, request):
#         serializer = MenuItemSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "Success", "data": serializer.data})
        
class menuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class singleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer