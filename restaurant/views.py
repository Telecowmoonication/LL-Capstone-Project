from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import User, Booking, MenuItem
from .serializers import UserSerializer, BookingSerializer, MenuItemSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


## This was in the course instructions at one point but then seems to get switched out for bookingViewSet
# class bookingView(APIView):
#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many=True)
#         return Response(serializer.data)
    

## This was in the course instructions at one point but then seems to get switched out for menuItemsView
# class menuview(APIView):
#     def post(self, request):
#         serializer = MenuItemSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "Success", "data": serializer.data})
        

class bookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class menuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    
class singleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer