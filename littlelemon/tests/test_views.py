from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=15.99, inventory=50)
        Menu.objects.create(title="Burger", price=12.50, inventory=75)
        
        # Initialize API client
        self.client = APIClient()
    
    def test_getall(self):
        """Test retrieving all menu items."""
        url = '/restaurant/menu/items'
        response = self.client.get(url)
        
        # Check if the response status is OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Get all Menu objects and serialize them
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        
        # Check if the serialized data equals the response
        self.assertEqual(response.data['results'], serializer.data)
    
    def test_create_menu_item(self):
        """Test creating a new menu item."""
        url = '/restaurant/menu/items'
        data = {
            'title': 'Greek Salad',
            'price': '12.99',
            'inventory': 30
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 4)
        self.assertEqual(Menu.objects.get(title='Greek Salad').price, 12.99)
    
    def test_search_menu_items(self):
        """Test searching menu items by title."""
        url = '/restaurant/menu/items?search=Pizza'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Pizza')
    
    def test_ordering_menu_items(self):
        """Test ordering menu items."""
        url = '/restaurant/menu/items?ordering=price'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        prices = [item['price'] for item in response.data['results']]
        self.assertEqual(prices, sorted(prices))


class BookingViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test bookings
        future_date = timezone.now() + timedelta(days=1)
        Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            BookingDate=future_date
        )
        Booking.objects.create(
            name="Jane Smith",
            no_of_guests=2,
            BookingDate=future_date + timedelta(days=1)
        )
        
        # Initialize API client
        self.client = APIClient()
    
    def test_list_bookings_requires_auth(self):
        """Test that listing bookings requires authentication."""
        url = '/restaurant/booking/tables/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_list_bookings_with_auth(self):
        """Test listing bookings with authentication."""
        self.client.force_authenticate(user=self.user)
        url = '/restaurant/booking/tables/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
    
    def test_create_booking_with_auth(self):
        """Test creating a booking with authentication."""
        self.client.force_authenticate(user=self.user)
        url = '/restaurant/booking/tables/'
        future_date = timezone.now() + timedelta(days=2)
        data = {
            'name': 'Test User',
            'no_of_guests': 3,
            'BookingDate': future_date.isoformat()
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 3)
    
    def test_upcoming_bookings(self):
        """Test the upcoming bookings endpoint."""
        self.client.force_authenticate(user=self.user)
        url = '/restaurant/booking/tables/upcoming/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # All test bookings are in the future
        self.assertEqual(len(response.data['results']), 2)

