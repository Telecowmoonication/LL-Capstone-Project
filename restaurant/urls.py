from django.urls import path, include
from .views import index, menuItemsView, singleMenuItemView, bookingView

urlpatterns = [
    path('', index, name='index'),
    path('menu', menuItemsView.as_view()),
    path('menu/<int:pk>', singleMenuItemView.as_view()),
]