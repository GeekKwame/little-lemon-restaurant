"""
Views for the restaurant API.

This module contains all API views for menu items and bookings.
"""
from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
import logging

logger = logging.getLogger('restaurant')


def index(request):
    """
    Homepage view that serves the static HTML template.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered HTML template
    """
    return render(request, 'index.html', {})


def menu_page(request):
    """
    Menu page view that displays all menu items.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered HTML template with menu items
    """
    menu_items = Menu.objects.all().order_by('title')
    return render(request, 'menu.html', {'menu_items': menu_items})


def booking_page(request):
    """
    Booking page view that displays the booking form and handles form submissions.
    
    Args:
        request: HTTP request object
        
    Returns:
        Rendered HTML template with booking form and success/error messages
    """
    message = None
    message_type = None
    
    if request.method == 'POST':
        try:
            from django.utils import timezone
            from django.contrib import messages
            
            name = request.POST.get('name')
            no_of_guests = request.POST.get('no_of_guests')
            booking_date = request.POST.get('BookingDate')
            
            # Validate required fields
            if not name or not no_of_guests or not booking_date:
                message = 'All fields are required.'
                message_type = 'error'
            else:
                try:
                    # Parse the booking date (datetime-local format: YYYY-MM-DDTHH:mm)
                    from datetime import datetime
                    # Convert to timezone-aware datetime
                    booking_datetime = datetime.strptime(booking_date, '%Y-%m-%dT%H:%M')
                    booking_datetime = timezone.make_aware(booking_datetime)
                    
                    # Validate number of guests
                    guests = int(no_of_guests)
                    if guests < 1 or guests > 20:
                        message = 'Number of guests must be between 1 and 20.'
                        message_type = 'error'
                    # Validate booking date is in the future
                    elif booking_datetime < timezone.now():
                        message = 'Booking date cannot be in the past.'
                        message_type = 'error'
                    else:
                        # Create the booking
                        booking = Booking.objects.create(
                            name=name.strip(),
                            no_of_guests=guests,
                            BookingDate=booking_datetime
                        )
                        message = f'Reservation successful! We look forward to seeing you on {booking_datetime.strftime("%B %d, %Y at %I:%M %p")}.'
                        message_type = 'success'
                        logger.info(f"Booking created via web form: {booking.name} for {booking.BookingDate}")
                except ValueError as ve:
                    message = f'Invalid date or number format: {str(ve)}'
                    message_type = 'error'
        except ValueError as e:
            message = f'Invalid input: {str(e)}'
            message_type = 'error'
        except Exception as e:
            message = f'An error occurred: {str(e)}'
            message_type = 'error'
            logger.error(f"Error creating booking: {e}")
    
    return render(request, 'booking.html', {
        'message': message,
        'message_type': message_type
    })


class MenuItemView(generics.ListCreateAPIView):
    """
    API view for listing and creating menu items.
    
    GET: Returns a paginated list of all menu items
    POST: Creates a new menu item
    
    Supports:
    - Pagination (10 items per page)
    - Search by title
    - Ordering by title, price, inventory
    - Filtering by price range
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]  # Public API
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title', 'price', 'inventory', 'created_at']
    ordering = ['title']
    filterset_fields = ['price']
    
    def perform_create(self, serializer):
        """Log menu item creation."""
        instance = serializer.save()
        logger.info(f"Menu item created: {instance.title} (ID: {instance.id})")
        return instance


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a single menu item.
    
    GET: Retrieve a menu item by ID
    PUT: Update a menu item (full update)
    PATCH: Update a menu item (partial update)
    DELETE: Delete a menu item
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]  # Public API
    
    def perform_update(self, serializer):
        """Log menu item update."""
        instance = serializer.save()
        logger.info(f"Menu item updated: {instance.title} (ID: {instance.id})")
        return instance
    
    def perform_destroy(self, instance):
        """Log menu item deletion."""
        logger.info(f"Menu item deleted: {instance.title} (ID: {instance.id})")
        instance.delete()


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing table bookings.
    
    Requires authentication for all operations.
    
    Supports:
    - List all bookings (GET /restaurant/booking/tables/)
    - Create new booking (POST /restaurant/booking/tables/)
    - Retrieve booking (GET /restaurant/booking/tables/{id}/)
    - Update booking (PUT/PATCH /restaurant/booking/tables/{id}/)
    - Delete booking (DELETE /restaurant/booking/tables/{id}/)
    - Filter by date range
    - Order by booking date
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['BookingDate', 'name', 'no_of_guests', 'created_at']
    ordering = ['-BookingDate']  # Most recent first
    filterset_fields = ['BookingDate', 'no_of_guests']
    
    def perform_create(self, serializer):
        """Log booking creation."""
        instance = serializer.save()
        logger.info(
            f"Booking created: {instance.name} for {instance.BookingDate} "
            f"(ID: {instance.id}, User: {self.request.user.username})"
        )
        return instance
    
    def perform_update(self, serializer):
        """Log booking update."""
        instance = serializer.save()
        logger.info(
            f"Booking updated: {instance.name} (ID: {instance.id}, "
            f"User: {self.request.user.username})"
        )
        return instance
    
    def perform_destroy(self, instance):
        """Log booking deletion."""
        logger.info(
            f"Booking deleted: {instance.name} (ID: {instance.id}, "
            f"User: {self.request.user.username})"
        )
        instance.delete()
    
    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        """
        Custom action to get upcoming bookings.
        
        GET /restaurant/booking/tables/upcoming/
        """
        from django.utils import timezone
        upcoming_bookings = self.queryset.filter(
            BookingDate__gte=timezone.now()
        ).order_by('BookingDate')
        
        page = self.paginate_queryset(upcoming_bookings)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(upcoming_bookings, many=True)
        return Response(serializer.data)