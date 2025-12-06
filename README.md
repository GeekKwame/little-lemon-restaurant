# Little Lemon Restaurant API

A production-ready Django REST Framework API for managing a restaurant's menu items and table bookings.

## 🚀 Features

- **Menu Management API**: Full CRUD operations for menu items
- **Booking Management API**: Secure table booking system with authentication
- **User Authentication**: Token-based authentication using Djoser
- **Production Ready**: Environment variables, logging, health checks, and comprehensive error handling
- **Comprehensive Testing**: Unit tests for models and views
- **API Documentation**: Browsable API interface
- **CORS Support**: Configured for frontend integration
- **Pagination & Filtering**: Built-in pagination, search, and filtering

## 📋 Requirements

- Python 3.8+
- MySQL 5.7+ or 8.0+
- Django 6.0
- Django REST Framework 3.16+

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/GeekKwame/little-lemon-restaurant.git
cd little-lemon-restaurant
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv env
env\Scripts\activate

# Linux/Mac
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=littlelemon_db
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=127.0.0.1
DB_PORT=3306

CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
```

### 5. Set Up MySQL Database

Create the database:

```sql
CREATE DATABASE littlelemon_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 6. Run Migrations

```bash
cd littlelemon
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Endpoints

### Menu API (Public)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/restaurant/menu/items/` | List all menu items (paginated) |
| POST | `/restaurant/menu/items/` | Create a new menu item |
| GET | `/restaurant/menu/items/{id}/` | Get a specific menu item |
| PUT | `/restaurant/menu/items/{id}/` | Update a menu item (full) |
| PATCH | `/restaurant/menu/items/{id}/` | Update a menu item (partial) |
| DELETE | `/restaurant/menu/items/{id}/` | Delete a menu item |

**Query Parameters:**
- `search`: Search by title (e.g., `?search=Pizza`)
- `ordering`: Order by field (e.g., `?ordering=price` or `?ordering=-price`)
- `page`: Page number for pagination

**Example Request:**
```bash
GET /restaurant/menu/items/?search=Pizza&ordering=price
```

### Booking API (Authenticated)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/restaurant/booking/tables/` | List all bookings (requires auth) |
| POST | `/restaurant/booking/tables/` | Create a new booking (requires auth) |
| GET | `/restaurant/booking/tables/{id}/` | Get a specific booking (requires auth) |
| PUT | `/restaurant/booking/tables/{id}/` | Update a booking (requires auth) |
| PATCH | `/restaurant/booking/tables/{id}/` | Partial update (requires auth) |
| DELETE | `/restaurant/booking/tables/{id}/` | Delete a booking (requires auth) |
| GET | `/restaurant/booking/tables/upcoming/` | Get upcoming bookings (requires auth) |

**Authentication:** Include header: `Authorization: Token <your_token>`

**Query Parameters:**
- `search`: Search by name
- `ordering`: Order by field (e.g., `?ordering=-BookingDate`)
- `BookingDate`: Filter by date
- `no_of_guests`: Filter by number of guests

**Example Request:**
```bash
GET /restaurant/booking/tables/?ordering=-BookingDate
Authorization: Token your-token-here
```

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/users/` | Register a new user |
| POST | `/api-token-auth/` | Get authentication token |
| POST | `/auth/token/login/` | Login with Djoser |
| POST | `/auth/token/logout/` | Logout (requires auth) |
| GET | `/auth/users/me/` | Get current user (requires auth) |

**Example Registration:**
```json
POST /auth/users/
{
    "username": "newuser",
    "password": "securepassword123",
    "email": "user@example.com"
}
```

**Example Login:**
```json
POST /api-token-auth/
{
    "username": "newuser",
    "password": "securepassword123"
}
```

**Response:**
```json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### System Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health/` | Health check endpoint |
| GET | `/api/info/` | API information |

## 🧪 Testing

Run all tests:

```bash
python manage.py test
```

Run specific test files:

```bash
python manage.py test tests.test_models
python manage.py test tests.test_views
```

Run with verbose output:

```bash
python manage.py test -v 2
```

## 📝 Example API Usage

### Using cURL

**Get Menu Items:**
```bash
curl http://127.0.0.1:8000/restaurant/menu/items/
```

**Create Menu Item:**
```bash
curl -X POST http://127.0.0.1:8000/restaurant/menu/items/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Greek Salad", "price": "12.99", "inventory": 30}'
```

**Get Token:**
```bash
curl -X POST http://127.0.0.1:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

**Create Booking (with token):**
```bash
curl -X POST http://127.0.0.1:8000/restaurant/booking/tables/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token your-token-here" \
  -d '{
    "name": "John Doe",
    "no_of_guests": 4,
    "BookingDate": "2025-12-15T19:00:00Z"
  }'
```

### Using Python Requests

```python
import requests

# Get menu items
response = requests.get('http://127.0.0.1:8000/restaurant/menu/items/')
print(response.json())

# Get token
response = requests.post('http://127.0.0.1:8000/api-token-auth/', json={
    'username': 'admin',
    'password': 'admin123'
})
token = response.json()['token']

# Create booking
headers = {'Authorization': f'Token {token}'}
response = requests.post(
    'http://127.0.0.1:8000/restaurant/booking/tables/',
    headers=headers,
    json={
        'name': 'John Doe',
        'no_of_guests': 4,
        'BookingDate': '2025-12-15T19:00:00Z'
    }
)
print(response.json())
```

## 🔒 Security Features

- **Token Authentication**: Secure API access with token-based authentication
- **Environment Variables**: Sensitive data stored in `.env` file
- **CORS Configuration**: Controlled cross-origin resource sharing
- **Input Validation**: Comprehensive validation on models and serializers
- **SQL Injection Protection**: Django ORM provides built-in protection
- **XSS Protection**: Django's built-in XSS protection
- **CSRF Protection**: Enabled for session-based authentication

## 📊 Database Models

### Menu
- `title`: CharField (max 255)
- `price`: DecimalField (max 10 digits, 2 decimal places)
- `inventory`: IntegerField (non-negative)
- `created_at`: DateTimeField (auto)
- `updated_at`: DateTimeField (auto)

### Booking
- `name`: CharField (max 255)
- `no_of_guests`: IntegerField (1-20)
- `BookingDate`: DateTimeField
- `created_at`: DateTimeField (auto)
- `updated_at`: DateTimeField (auto)

## 🏗️ Project Structure

```
little-lemon-restaurant/
├── littlelemon/
│   ├── manage.py
│   ├── littlelemon/
│   │   ├── settings.py      # Django settings
│   │   ├── urls.py          # URL configuration
│   │   └── ...
│   ├── restaurant/
│   │   ├── models.py        # Database models
│   │   ├── views.py         # API views
│   │   ├── serializers.py  # DRF serializers
│   │   ├── exceptions.py    # Custom exception handlers
│   │   └── health_views.py  # Health check endpoints
│   ├── tests/
│   │   ├── test_models.py  # Model tests
│   │   └── test_views.py   # View tests
│   └── logs/               # Application logs
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## 🚀 Production Deployment

### Environment Variables for Production

```env
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_NAME=production_db
DB_USER=production_user
DB_PASSWORD=secure-password
DB_HOST=your-db-host
```

### Security Checklist

- [ ] Set `DEBUG=False`
- [ ] Use strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use HTTPS (SSL/TLS)
- [ ] Set secure database credentials
- [ ] Enable CORS only for trusted origins
- [ ] Set up proper logging
- [ ] Configure static files serving
- [ ] Set up database backups
- [ ] Configure rate limiting (if needed)

## 📖 Documentation

- **Django Documentation**: https://docs.djangoproject.com/
- **Django REST Framework**: https://www.django-rest-framework.org/
- **Djoser Documentation**: https://djoser.readthedocs.io/

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is part of a course assignment.

## 👤 Author

**GeekKwame**
- GitHub: [@GeekKwame](https://github.com/GeekKwame)

## 🙏 Acknowledgments

- Django REST Framework team
- Djoser contributors
- All course instructors and peers

---

**Status**: ✅ Production Ready

**Last Updated**: December 2025

