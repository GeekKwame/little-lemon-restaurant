"""
Health check and system status views.
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.http import JsonResponse


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """
    Health check endpoint for monitoring and load balancers.
    
    Returns:
        JSON response with system status
    """
    try:
        # Check database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            db_status = "healthy"
    except Exception as e:
        db_status = f"unhealthy: {str(e)}"
    
    return Response({
        'status': 'healthy' if db_status == "healthy" else 'degraded',
        'database': db_status,
        'service': 'Little Lemon Restaurant API',
        'version': '1.0.0'
    }, status=status.HTTP_200_OK if db_status == "healthy" else status.HTTP_503_SERVICE_UNAVAILABLE)


@api_view(['GET'])
@permission_classes([AllowAny])
def api_info(request):
    """
    API information endpoint.
    
    Returns:
        JSON response with API details and available endpoints
    """
    return Response({
        'name': 'Little Lemon Restaurant API',
        'version': '1.0.0',
        'description': 'REST API for Little Lemon Restaurant menu and booking management',
        'endpoints': {
            'menu': {
                'list': '/restaurant/menu/items/',
                'detail': '/restaurant/menu/items/{id}/',
                'methods': ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
            },
            'bookings': {
                'list': '/restaurant/booking/tables/',
                'detail': '/restaurant/booking/tables/{id}/',
                'upcoming': '/restaurant/booking/tables/upcoming/',
                'methods': ['GET', 'POST', 'PUT', 'PATCH', 'DELETE'],
                'authentication': 'Required (Token)'
            },
            'authentication': {
                'register': '/auth/users/',
                'login': '/api-token-auth/',
                'djoser_login': '/auth/token/login/',
                'methods': ['POST']
            },
            'health': {
                'check': '/api/health/',
                'info': '/api/info/'
            }
        }
    })

