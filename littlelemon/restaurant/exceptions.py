"""
Custom exception handlers for the restaurant API.
"""
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger('restaurant')


def custom_exception_handler(exc, context):
    """
    Custom exception handler that provides consistent error responses.
    """
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)

    # Log the exception
    logger.error(f"Exception occurred: {exc}", exc_info=True)

    # Customize the response
    if response is not None:
        custom_response_data = {
            'error': {
                'status_code': response.status_code,
                'message': 'An error occurred',
                'details': response.data
            }
        }
        response.data = custom_response_data

    return response

