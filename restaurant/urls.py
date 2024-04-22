from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import index, msg,menuItemsView, singleMenuItemView, bookingViewSet

urlpatterns = [
    path('', index, name='index'), # Endpoint: restaurant/index
    path('message', msg, name='message'), # Endpoint(needs auth): restaurant/message
    path('api-token-auth', obtain_auth_token), # Endpoint: restaurant/api-token-auth (This is to get a token so you can access pages that need authentication)
    path('menu', menuItemsView.as_view(), name='menu'), # Endpoint: restaurant/menu
    path('menu/<int:pk>', singleMenuItemView.as_view()), # Endpoint: restaurant/menu/pk
    
]