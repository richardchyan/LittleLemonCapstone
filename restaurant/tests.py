from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from restaurant.models import Menu

# Create your tests here.

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price = 80, inventory=100)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "IceCream: 80")

    def test_get_chocolate(self):
        chocolate = Menu.objects.create(title='MilkChocolate', price = 15, inventory = 5000)
        chocolatestr = chocolate.get_item()
        self.assertEqual(chocolatestr, "MilkChocolate: 15")

class MenuViewTest(TestCase):
    def setup(self):
        # Adding objects 
        Menu.objects.create(name='GreenTeaIceCream', price=20)
        Menu.objects.create(name='VanillaIceCream', price=20)
        Menu.objects.create(name='PralinesIceCream', price=20)

def test_getall(self):
        # Retrieve all Menu objects
        url = reverse('menu-list')  
        # Assuming 'menu-list' is the URL name for listing all Menu objects
        response = self.client.get(url)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected data
        self.assertQuerysetEqual(
            response.context['menu_list'],
            ['<Menu: Item1>', '<Menu: Item2>'],
            ordered=False
        )