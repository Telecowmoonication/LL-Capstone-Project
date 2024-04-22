from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Ice Cream", price=2.50, inventory=125)
        self.assertEqual(item.get_item(), "Ice Cream : 2.50")