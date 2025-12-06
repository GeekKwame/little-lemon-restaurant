from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.

class Menu(models.Model):
    """
    Menu model representing a menu item in the restaurant.
    
    Attributes:
        title: Name of the menu item
        price: Price of the item (must be positive)
        inventory: Number of items available (must be non-negative)
        created_at: Timestamp when the item was created
        updated_at: Timestamp when the item was last updated
    """
    title = models.CharField(
        max_length=255,
        help_text="Name of the menu item"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        help_text="Price of the item (must be greater than 0)"
    )
    inventory = models.IntegerField(
        validators=[MinValueValidator(0)],
        help_text="Number of items available in inventory"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.title} : ${str(self.price)}'
    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu Items'
        ordering = ['title']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['price']),
        ]


class Booking(models.Model):
    """
    Booking model representing a table reservation.
    
    Attributes:
        name: Name of the person making the booking
        no_of_guests: Number of guests (must be between 1 and 20)
        BookingDate: Date and time of the reservation
        created_at: Timestamp when the booking was created
        updated_at: Timestamp when the booking was last updated
    """
    name = models.CharField(
        max_length=255,
        help_text="Name of the person making the reservation"
    )
    no_of_guests = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        help_text="Number of guests (1-20)"
    )
    BookingDate = models.DateTimeField(
        help_text="Date and time of the reservation"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name} - {self.BookingDate.strftime("%Y-%m-%d %H:%M")}'
    
    def clean(self):
        """Validate that booking date is in the future."""
        from django.core.exceptions import ValidationError
        if self.BookingDate and self.BookingDate < timezone.now():
            raise ValidationError('Booking date cannot be in the past.')
    
    def save(self, *args, **kwargs):
        """Override save to call clean validation."""
        self.full_clean()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking Records'
        ordering = ['BookingDate']
        indexes = [
            models.Index(fields=['BookingDate']),
            models.Index(fields=['name']),
        ]