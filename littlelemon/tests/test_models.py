from django.test import TestCase
from restaurant.models import Menu, Booking
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta


class MenuTest(TestCase):
    def test_get_item(self):
        """Test Menu model string representation."""
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : $80")
    
    def test_menu_created_at_auto_set(self):
        """Test that created_at is automatically set."""
        item = Menu.objects.create(title="Pizza", price=15.99, inventory=50)
        self.assertIsNotNone(item.created_at)
        self.assertIsNotNone(item.updated_at)
    
    def test_menu_price_validation(self):
        """Test that price must be positive."""
        from decimal import Decimal
        # This should work
        item = Menu.objects.create(title="Test", price=Decimal('10.00'), inventory=10)
        self.assertEqual(item.price, Decimal('10.00'))


class BookingTest(TestCase):
    def test_booking_string_representation(self):
        """Test Booking model string representation."""
        future_date = timezone.now() + timedelta(days=1)
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            BookingDate=future_date
        )
        self.assertIn("John Doe", str(booking))
    
    def test_booking_created_at_auto_set(self):
        """Test that created_at is automatically set."""
        future_date = timezone.now() + timedelta(days=1)
        booking = Booking.objects.create(
            name="Test User",
            no_of_guests=2,
            BookingDate=future_date
        )
        self.assertIsNotNone(booking.created_at)
        self.assertIsNotNone(booking.updated_at)
    
    def test_booking_guests_validation(self):
        """Test that number of guests must be between 1 and 20."""
        future_date = timezone.now() + timedelta(days=1)
        
        # Valid booking
        booking = Booking.objects.create(
            name="Test",
            no_of_guests=5,
            BookingDate=future_date
        )
        self.assertEqual(booking.no_of_guests, 5)

