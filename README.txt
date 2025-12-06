Little Lemon Restaurant - API Endpoints

This document contains all API paths that should be tested for the peer review.

================================================================================
SETUP INSTRUCTIONS
================================================================================

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies: pip install -r requirements.txt
4. Configure MySQL database in settings.py
5. Run migrations: python manage.py migrate
6. Create superuser: python manage.py createsuperuser
7. Start server: python manage.py runserver
8. Server will run at: http://127.0.0.1:8000/

================================================================================
API ENDPOINTS FOR TESTING
================================================================================

BASE URL: http://127.0.0.1:8000

--------------------------------------------------------------------------------
1. HOMEPAGE (Static HTML Content)
--------------------------------------------------------------------------------
GET /
GET /restaurant/

Description: Django serves static HTML content for the Little Lemon restaurant homepage.

--------------------------------------------------------------------------------
2. MENU API (Public - No Authentication Required)
--------------------------------------------------------------------------------
GET    /restaurant/menu/items
POST   /restaurant/menu/items
GET    /restaurant/menu/items/<id>
PUT    /restaurant/menu/items/<id>
DELETE /restaurant/menu/items/<id>

Description: CRUD operations for menu items.

Example POST Request Body:
{
    "title": "Grilled Salmon",
    "price": "25.99",
    "inventory": 50
}

--------------------------------------------------------------------------------
3. BOOKING API (Secured - Authentication Required)
--------------------------------------------------------------------------------
GET    /restaurant/booking/tables/
POST   /restaurant/booking/tables/
GET    /restaurant/booking/tables/<id>/
PUT    /restaurant/booking/tables/<id>/
PATCH  /restaurant/booking/tables/<id>/
DELETE /restaurant/booking/tables/<id>/

Description: CRUD operations for table bookings. Requires token authentication.

Authentication: Include header: Authorization: Token <your_token>

Example POST Request Body:
{
    "name": "John Doe",
    "no_of_guests": 4,
    "BookingDate": "2025-12-15T19:00:00Z"
}

--------------------------------------------------------------------------------
4. USER REGISTRATION (Public)
--------------------------------------------------------------------------------
POST   /auth/users/
GET    /auth/users/ (requires authentication)
GET    /auth/users/me/ (requires authentication)
PUT    /auth/users/me/ (requires authentication)
PATCH  /auth/users/me/ (requires authentication)
DELETE /auth/users/me/ (requires authentication)

Description: User registration and management using Djoser.

Example POST Request Body (Registration):
{
    "username": "newuser",
    "password": "securepassword123",
    "email": "user@example.com"
}

--------------------------------------------------------------------------------
5. TOKEN AUTHENTICATION
--------------------------------------------------------------------------------
POST   /api-token-auth/
POST   /auth/token/login/
POST   /auth/token/logout/ (requires authentication)

Description: Obtain authentication token for API access.

Example POST Request Body (/api-token-auth/):
{
    "username": "admin",
    "password": "admin123"
}

Response:
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}

Use this token in Authorization header: Token <token>

--------------------------------------------------------------------------------
6. ADMIN PANEL
--------------------------------------------------------------------------------
GET    /admin/

Description: Django admin interface for managing Menu and Booking records.

Login with superuser credentials created during setup.

================================================================================
TESTING WITH INSOMNIA REST CLIENT
================================================================================

1. GET TOKEN:
   - Method: POST
   - URL: http://127.0.0.1:8000/api-token-auth/
   - Body (JSON): {"username": "admin", "password": "admin123"}
   - Copy the token from response

2. TEST MENU API (No Auth Required):
   - GET http://127.0.0.1:8000/restaurant/menu/items
   - POST http://127.0.0.1:8000/restaurant/menu/items
     Body: {"title": "Pizza", "price": "15.99", "inventory": 50}

3. TEST BOOKING API (Auth Required):
   - Add Header: Authorization: Token <your_token>
   - GET http://127.0.0.1:8000/restaurant/booking/tables/
   - POST http://127.0.0.1:8000/restaurant/booking/tables/
     Body: {"name": "Jane Smith", "no_of_guests": 2, "BookingDate": "2025-12-16T18:00:00Z"}

4. TEST USER REGISTRATION:
   - POST http://127.0.0.1:8000/auth/users/
     Body: {"username": "testuser", "password": "testpass123", "email": "test@example.com"}

================================================================================
UNIT TESTS
================================================================================

Run unit tests with:
python manage.py test

Test files located in: tests/
- tests/test_models.py (Menu model tests)
- tests/test_views.py (Menu API view tests)

================================================================================
DATABASE
================================================================================

Database: MySQL
Database Name: littlelemon_db
Connection configured in: littlelemon/settings.py

Models:
- Menu (title, price, inventory)
- Booking (name, no_of_guests, BookingDate)

================================================================================
PROJECT REQUIREMENTS CHECKLIST
================================================================================

✓ Django serves static HTML content
✓ Project committed to Git repository
✓ Application connects to MySQL database
✓ Menu API implemented (CRUD operations)
✓ Table booking API implemented (CRUD operations)
✓ User registration and authentication set up (Djoser)
✓ Unit tests included (test_models.py, test_views.py)
✓ API can be tested with Insomnia REST client

================================================================================
END OF README
================================================================================

