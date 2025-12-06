from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=15.99, inventory=50)
        Menu.objects.create(title="Burger", price=12.50, inventory=75)
        
        # Initialize API client
        self.client = APIClient()
    
    def test_getall(self):
        # Retrieve all Menu objects
        url = '/restaurant/menu/items'
        response = self.client.get(url)
        
        # Check if the response status is OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Get all Menu objects and serialize them
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        
        # Check if the serialized data equals the response
        self.assertEqual(response.data, serializer.data)

