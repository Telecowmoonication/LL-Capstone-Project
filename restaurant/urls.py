from django.urls import path, include
from .views import index, menuItemsView, singleMenuItemView, bookingViewSet

urlpatterns = [
    path('', index, name='index'), # Endpoint: restaurant/index
    path('menu', menuItemsView.as_view()), # Endpoint: restaurant/menu
    path('menu/<int:pk>', singleMenuItemView.as_view()), # Endpoint: restaurant/menu/pk
]