from rest_framework import serializers
from .models import Menu, Booking
from django.utils import timezone


class MenuSerializer(serializers.ModelSerializer):
    """
    Serializer for Menu model.
    
    Provides validation and serialization for menu items.
    """
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        coerce_to_string=False
    )
    
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_price(self, value):
        """Validate that price is positive."""
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
    
    def validate_inventory(self, value):
        """Validate that inventory is non-negative."""
        if value < 0:
            raise serializers.ValidationError("Inventory cannot be negative.")
        return value


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for Booking model.
    
    Provides validation and serialization for table bookings.
    """
    class Meta:
        model = Booking
        fields = ['id', 'name', 'no_of_guests', 'BookingDate', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_no_of_guests(self, value):
        """Validate number of guests is between 1 and 20."""
        if value < 1:
            raise serializers.ValidationError("Number of guests must be at least 1.")
        if value > 20:
            raise serializers.ValidationError("Number of guests cannot exceed 20.")
        return value
    
    def validate_BookingDate(self, value):
        """Validate that booking date is in the future."""
        if value < timezone.now():
            raise serializers.ValidationError("Booking date cannot be in the past.")
        return value

