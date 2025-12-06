# Peer Review Submission Guide

## ✅ Project Ready for Peer Review

Your Little Lemon Restaurant project has been prepared and pushed to GitHub for peer review.

---

## 📋 Grading Criteria Checklist

### ✅ All Requirements Met:

1. **✓ Django serves static HTML content**
   - Homepage available at: `http://127.0.0.1:8000/`
   - Template: `littlelemon/littlelemon/templates/index.html`

2. **✓ Project committed to Git repository**
   - Repository: `https://github.com/GeekKwame/little-lemon-restaurant.git`
   - All files committed and pushed

3. **✓ Application connects to MySQL database**
   - Database: `littlelemon_db`
   - Configuration in: `littlelemon/littlelemon/settings.py`
   - Models: `Menu` and `Booking`

4. **✓ Menu API implemented**
   - Endpoints: `/restaurant/menu/items`
   - CRUD operations: GET, POST, PUT, DELETE
   - No authentication required

5. **✓ Table booking API implemented**
   - Endpoints: `/restaurant/booking/tables/`
   - CRUD operations: GET, POST, PUT, PATCH, DELETE
   - Uses ModelViewSet with DefaultRouter

6. **✓ User registration and authentication set up**
   - Djoser integration: `/auth/users/`
   - Token authentication: `/api-token-auth/` and `/auth/token/login/`
   - Booking API secured with token authentication

7. **✓ Unit tests included**
   - Test folder: `littlelemon/tests/`
   - Files: `test_models.py` and `test_views.py`
   - All tests passing ✅

8. **✓ API can be tested with Insomnia REST client**
   - All endpoints documented in `README.txt`
   - Authentication instructions included
   - Example requests provided

---

## 📄 README.txt File

The `README.txt` file has been created and pushed to GitHub. It contains:

- All API endpoints for testing
- Setup instructions
- Authentication requirements
- Example request bodies
- Insomnia REST client testing guide
- Unit tests information
- Database configuration details

**Location in repository:** `/README.txt`

---

## 🔗 GitHub Repository

**Repository URL:** `https://github.com/GeekKwame/little-lemon-restaurant.git`

**Branch:** `master`

**Latest Commit:** Includes README.txt and unit tests

---

## 📝 Submission Steps

### Step 1: Click on "My submission" tab
- Navigate to the course submission page
- Click on the "My submission" tab

### Step 2: Provide Project Title
**Suggested Title:**
```
Back-end developer capstone project
```

Or you can use:
```
Little Lemon Restaurant API - Django REST Framework
```

### Step 3: Paste GitHub Repository URL
**Repository URL:**
```
https://github.com/GeekKwame/little-lemon-restaurant.git
```

---

## 🧪 What Peers Will Test

Based on the `README.txt` file, peers will test:

### 1. Static HTML Content
- **URL:** `http://127.0.0.1:8000/`
- **Expected:** Little Lemon restaurant homepage

### 2. Menu API (Public)
- **GET** `/restaurant/menu/items` - List all menu items
- **POST** `/restaurant/menu/items` - Create menu item
- **GET** `/restaurant/menu/items/<id>` - Get single item
- **PUT** `/restaurant/menu/items/<id>` - Update item
- **DELETE** `/restaurant/menu/items/<id>` - Delete item

### 3. Booking API (Secured)
- **GET** `/restaurant/booking/tables/` - List bookings (requires auth)
- **POST** `/restaurant/booking/tables/` - Create booking (requires auth)
- **GET** `/restaurant/booking/tables/<id>/` - Get single booking
- **PUT** `/restaurant/booking/tables/<id>/` - Update booking
- **DELETE** `/restaurant/booking/tables/<id>/` - Delete booking

### 4. User Registration
- **POST** `/auth/users/` - Register new user

### 5. Token Authentication
- **POST** `/api-token-auth/` - Get authentication token
- **POST** `/auth/token/login/` - Login with Djoser

### 6. Unit Tests
- Run: `python manage.py test`
- Verify: All tests pass

### 7. Insomnia Testing
- Test all endpoints with Insomnia REST client
- Verify authentication works correctly

---

## 📊 Project Structure

```
little-lemon-restaurant/
├── README.txt                    ← API endpoints for peers
├── littlelemon/
│   ├── manage.py
│   ├── tests/                    ← Unit tests
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   └── test_views.py
│   ├── littlelemon/
│   │   ├── settings.py          ← MySQL configuration
│   │   ├── urls.py               ← All URL routes
│   │   └── templates/
│   │       └── index.html        ← Static HTML
│   └── restaurant/
│       ├── models.py             ← Menu & Booking models
│       ├── views.py              ← API views
│       ├── serializers.py        ← DRF serializers
│       └── urls.py               ← App URLs
└── .gitignore
```

---

## ✅ Final Verification

Before submitting, verify:

- [x] README.txt is in the repository root
- [x] All code is committed and pushed
- [x] Unit tests are included and passing
- [x] MySQL database configuration is correct
- [x] All API endpoints are documented
- [x] Authentication is properly configured
- [x] Project can be cloned and run by peers

---

## 🎯 Key API Endpoints Summary

For quick reference, here are the main endpoints:

| Endpoint | Method | Auth Required | Purpose |
|----------|--------|---------------|---------|
| `/` | GET | No | Homepage |
| `/restaurant/menu/items` | GET, POST | No | Menu API |
| `/restaurant/menu/items/<id>` | GET, PUT, DELETE | No | Single menu item |
| `/restaurant/booking/tables/` | GET, POST | ✅ Yes | Booking API |
| `/restaurant/booking/tables/<id>/` | GET, PUT, PATCH, DELETE | ✅ Yes | Single booking |
| `/auth/users/` | POST | No | User registration |
| `/api-token-auth/` | POST | No | Get token |
| `/auth/token/login/` | POST | No | Djoser login |

---

## 🚀 Ready to Submit!

Your project is complete and ready for peer review. All requirements have been met:

✅ Django static HTML content  
✅ Git repository with all commits  
✅ MySQL database connection  
✅ Menu API implemented  
✅ Booking API implemented  
✅ User registration and authentication  
✅ Unit tests included  
✅ Insomnia REST client testing ready  

**Next Step:** Submit the GitHub repository URL in the course submission page.

---

**Good luck with your peer review! 🎉**

