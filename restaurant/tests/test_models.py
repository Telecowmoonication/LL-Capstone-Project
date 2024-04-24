from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.menu_item = MenuItem.objects.create(title="Ice Cream", price=2.50, inventory=125)
    
    def test_menu_item_str(self):
        self.assertEqual(str(self.menu_item), "Ice Cream : 2.50")