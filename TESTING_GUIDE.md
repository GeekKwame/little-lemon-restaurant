# Little Lemon Restaurant - Application Testing Guide

## 🚀 Server Status

The Django development server should be running at: `http://127.0.0.1:8000/`

---

## 📋 Testing Checklist

### ✅ 1. Homepage Test
**URL:** `http://127.0.0.1:8000/` or `http://127.0.0.1:8000/restaurant/`

**Expected:** Little Lemon Restaurant homepage with navigation and content

---

### ✅ 2. Admin Panel Test
**URL:** `http://127.0.0.1:8000/admin/`

**Credentials:**
- Username: `admin`
- Password: `admin123`

**What to check:**
- ✅ Login successful
- ✅ See "TOKENS" section in dashboard
- ✅ See "Menu Items" and "Booking Records" sections
- ✅ Can add/edit Menu and Booking data

---

### ✅ 3. Menu API Tests

#### Test 3.1: List Menu Items (GET)
**URL:** `http://127.0.0.1:8000/restaurant/menu/items`

**Method:** GET

**Expected:** List of menu items (or empty array)

**Test in Browser:**
- Open URL in browser
- Should see browsable API interface
- Click "GET" button

**Test with cURL:**
```bash
curl http://127.0.0.1:8000/restaurant/menu/items
```

#### Test 3.2: Create Menu Item (POST)
**URL:** `http://127.0.0.1:8000/restaurant/menu/items`

**Method:** POST

**Body (JSON):**
```json
{
    "title": "Grilled Salmon",
    "price": "25.99",
    "inventory": 50
}
```

**Expected:** Created menu item with ID

**Test in Browser:**
- Use browsable API form
- Enter JSON data
- Click "POST"

#### Test 3.3: Get Single Menu Item (GET)
**URL:** `http://127.0.0.1:8000/restaurant/menu/items/1`

**Method:** GET

**Expected:** Single menu item details

#### Test 3.4: Update Menu Item (PUT)
**URL:** `http://127.0.0.1:8000/restaurant/menu/items/1`

**Method:** PUT

**Body (JSON):**
```json
{
    "title": "Grilled Salmon",
    "price": "29.99",
    "inventory": 45
}
```

**Expected:** Updated menu item

#### Test 3.5: Delete Menu Item (DELETE)
**URL:** `http://127.0.0.1:8000/restaurant/menu/items/1`

**Method:** DELETE

**Expected:** 204 No Content (item deleted)

---

### ✅ 4. Booking API Tests (Secured - Requires Authentication)

#### Test 4.1: Get Token First
**URL:** `http://127.0.0.1:8000/api-token-auth/`

**Method:** POST

**Body (JSON):**
```json
{
    "username": "admin",
    "password": "admin123"
}
```

**Expected Response:**
```json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

**Save this token for next tests!**

#### Test 4.2: List Bookings (GET) - Without Token (Should Fail)
**URL:** `http://127.0.0.1:8000/restaurant/booking/tables/`

**Method:** GET

**Expected:** `401 Unauthorized`

**Response:**
```json
{
    "detail": "Authentication credentials were not provided."
}
```

#### Test 4.3: List Bookings (GET) - With Token (Should Succeed)
**URL:** `http://127.0.0.1:8000/restaurant/booking/tables/`

**Method:** GET

**Headers:**
```
Authorization: Token YOUR_TOKEN_HERE
```

**Expected:** List of bookings (or empty array)

**Test with cURL:**
```bash
curl -H "Authorization: Token YOUR_TOKEN_HERE" \
     http://127.0.0.1:8000/restaurant/booking/tables/
```

#### Test 4.4: Create Booking (POST) - With Token
**URL:** `http://127.0.0.1:8000/restaurant/booking/tables/`

**Method:** POST

**Headers:**
```
Authorization: Token YOUR_TOKEN_HERE
Content-Type: application/json
```

**Body (JSON):**
```json
{
    "name": "John Doe",
    "no_of_guests": 4,
    "BookingDate": "2025-12-15T19:00:00Z"
}
```

**Expected:** Created booking object

#### Test 4.5: Get Single Booking (GET) - With Token
**URL:** `http://127.0.0.1:8000/restaurant/booking/tables/1/`

**Method:** GET

**Headers:**
```
Authorization: Token YOUR_TOKEN_HERE
```

**Expected:** Single booking details

---

### ✅ 5. User Registration & Authentication Tests

#### Test 5.1: Register New User
**URL:** `http://127.0.0.1:8000/auth/users/`

**Method:** POST

**Body (JSON):**
```json
{
    "username": "testuser",
    "password": "testpass123",
    "email": "test@example.com"
}
```

**Expected:** User created with ID

#### Test 5.2: List Users
**URL:** `http://127.0.0.1:8000/auth/users/`

**Method:** GET

**Expected:** List of all users

#### Test 5.3: Login with Djoser (Get Token)
**URL:** `http://127.0.0.1:8000/auth/token/login/`

**Method:** POST

**Body (JSON):**
```json
{
    "username": "testuser",
    "password": "testpass123"
}
```

**Expected:** Token response

#### Test 5.4: Get Current User
**URL:** `http://127.0.0.1:8000/auth/users/me/`

**Method:** GET

**Headers:**
```
Authorization: Token YOUR_TOKEN_HERE
```

**Expected:** Current user details

#### Test 5.5: Logout
**URL:** `http://127.0.0.1:8000/auth/token/logout/`

**Method:** POST

**Headers:**
```
Authorization: Token YOUR_TOKEN_HERE
```

**Expected:** 204 No Content

---

## 🧪 Quick Test Commands

### Test Menu API:
```bash
# List items
curl http://127.0.0.1:8000/restaurant/menu/items

# Create item
curl -X POST http://127.0.0.1:8000/restaurant/menu/items \
  -H "Content-Type: application/json" \
  -d '{"title": "Greek Salad", "price": "12.99", "inventory": 30}'
```

### Test Booking API (Secured):
```bash
# Get token first
curl -X POST http://127.0.0.1:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'

# Use token to access bookings
curl -H "Authorization: Token YOUR_TOKEN" \
     http://127.0.0.1:8000/restaurant/booking/tables/

# Create booking
curl -X POST http://127.0.0.1:8000/restaurant/booking/tables/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Smith", "no_of_guests": 2, "BookingDate": "2025-12-16T18:00:00Z"}'
```

### Test User Registration:
```bash
# Register user
curl -X POST http://127.0.0.1:8000/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{"username": "newuser", "password": "pass123", "email": "user@example.com"}'

# Login
curl -X POST http://127.0.0.1:8000/auth/token/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "newuser", "password": "pass123"}'
```

---

## 📊 Expected Results Summary

| Endpoint | Method | Auth Required | Expected Status |
|----------|--------|---------------|-----------------|
| `/` | GET | No | 200 OK |
| `/admin/` | GET | Yes (Admin) | 200 OK |
| `/restaurant/menu/items` | GET | No | 200 OK |
| `/restaurant/menu/items` | POST | No | 201 Created |
| `/restaurant/booking/tables/` | GET | ✅ Yes | 200 OK (with token) |
| `/restaurant/booking/tables/` | GET | ❌ No | 401 Unauthorized |
| `/restaurant/booking/tables/` | POST | ✅ Yes | 201 Created (with token) |
| `/api-token-auth/` | POST | No | 200 OK (returns token) |
| `/auth/users/` | POST | No | 201 Created |
| `/auth/token/login/` | POST | No | 200 OK (returns token) |

---

## 🔍 Verification Steps

1. ✅ Server is running (check terminal output)
2. ✅ Homepage loads correctly
3. ✅ Admin panel accessible
4. ✅ Menu API works (GET, POST)
5. ✅ Booking API requires authentication
6. ✅ Token authentication works
7. ✅ User registration works
8. ✅ All endpoints respond correctly

---

## 🐛 Troubleshooting

### Server not starting?
- Check if port 8000 is already in use
- Verify virtual environment is activated
- Check for any error messages

### 401 Unauthorized errors?
- Make sure you're including the token in Authorization header
- Verify token format: `Token <token>` (not Bearer)
- Check if token is valid (not expired/deleted)

### 404 Not Found?
- Verify URL paths are correct
- Check that migrations are applied
- Ensure server is running

### 500 Internal Server Error?
- Check Django logs in terminal
- Verify database connection
- Check settings.py configuration

---

## ✅ Testing Complete!

Once all tests pass, your application is fully functional with:
- ✅ Menu API (public)
- ✅ Booking API (secured)
- ✅ User registration
- ✅ Token authentication
- ✅ Admin panel

Happy testing! 🎉

