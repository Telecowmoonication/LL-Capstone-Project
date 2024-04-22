from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    
    def setUp(self):
        MenuItem.objects.create(title="Lemon Cake", price=3.00, inventory=25)
        MenuItem.objects.create(title="Strawberry Lemonade", price=2.50, inventory= 75)
        
    def test_get_all_menu_items(self):
        client = APIClient()
        response = client.get(reverse('menu'))
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        
        # Create the expected paginated response structure to prevent errors while testing
        expected_response = {
            'count' : len(serializer.data),
            'next': None,
            'previous' : None,
            'results' : serializer.data
        }
        
        print("Response Data:", response.data)  # Debugging output
        print("Expected Serialized Data:", expected_response)  # Debugging output
        
        self.assertEqual(response.data, expected_response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)