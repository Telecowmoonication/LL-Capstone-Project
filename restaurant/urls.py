from django.urls import path
from rest_framework.authtoken import views
from .views import index, msg, menuItemsView, singleMenuItemView, userRegistrationView

urlpatterns = [
    path('', index, name='index'), # Endpoint: restaurant/
    path('message', msg, name='message'), # Endpoint(needs auth): restaurant/message
    path('register', userRegistrationView.as_view(), name='user-register'), # Endpoint: restaurant/register (To create account and be able to generate an auth token with endpoint below)
    path('api-token-auth', views.obtain_auth_token), # Endpoint: restaurant/api-token-auth (This is to get a token so you can access pages that need authentication)
    path('menu', menuItemsView.as_view(), name='menu'), # Endpoint(needs auth): restaurant/menu
    path('menu/<int:pk>', singleMenuItemView.as_view()), # Endpoint(needs auth): restaurant/menu/pk
    
]