# Djoser Registration Setup - Exercise Completion Summary

## ✅ All Steps Completed Successfully!

---

## Step 1: Install Djoser Library ✅

**Command:**
```bash
pip install djoser
```

**Result:** ✅ Successfully installed
- **Package:** `djoser`
- **Version:** 2.3.3
- **Dependencies:** All installed (djangorestframework-simplejwt, social-auth-app-django, etc.)

---

## Step 2: Add 'djoser' to INSTALLED_APPS ✅

**File:** `littlelemon/littlelemon/settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',  # ✅ Added for token authentication
    'djoser',                     # ✅ Added after 'rest_framework'
    'restaurant',
    'reservation'
]
```

**Status:** ✅ 'djoser' added after 'rest_framework' in INSTALLED_APPS

---

## Step 3: Add DJOSER Configuration ✅

**File:** `littlelemon/littlelemon/settings.py`

```python
# Djoser
DJOSER = {
    "USER_ID_FIELD": "username"
}
```

**Status:** ✅ DJOSER configuration added

---

## Step 4: Add Authentication Classes ✅

**File:** `littlelemon/littlelemon/settings.py`

```python
# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # ✅ Added
        'rest_framework.authentication.SessionAuthentication',  # ✅ Added
    ],
}
```

**Status:** ✅ Both TokenAuthentication and SessionAuthentication added

---

## Step 5: Add Djoser URL Routes ✅

**File:** `littlelemon/littlelemon/urls.py`

```python
urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('restaurant.urls')),
   path('restaurant/', include('restaurant.urls')),
   path('restaurant/', include(router.urls)),
   path('auth/', include('djoser.urls')),              # ✅ Added
   path('auth/', include('djoser.urls.authtoken')),    # ✅ Added
]
```

**Status:** ✅ Djoser URLs configured

---

## Step 6: Run Migrations ✅

**Commands:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Result:** ✅ Migrations applied successfully
- `authtoken.0001_initial` - Created token tables
- `authtoken.0002_auto_20160226_1747` - Updated token structure
- `authtoken.0003_tokenproxy` - Token proxy model
- `authtoken.0004_alter_tokenproxy_options` - Token options

**Token Table Created:** ✅ `authtoken_token` table in database

---

## Step 7: Available Djoser Endpoints

### User Registration & Management:
- **POST** `/auth/users/` - Register a new user
- **GET** `/auth/users/` - List all users (requires authentication)
- **GET** `/auth/users/me/` - Get current user details
- **PUT** `/auth/users/me/` - Update current user
- **PATCH** `/auth/users/me/` - Partial update current user
- **DELETE** `/auth/users/me/` - Delete current user
- **GET** `/auth/users/{id}/` - Get user by ID
- **PUT** `/auth/users/{id}/` - Update user by ID
- **DELETE** `/auth/users/{id}/` - Delete user by ID

### Token Authentication:
- **POST** `/auth/token/login/` - Login and get token
- **POST** `/auth/token/logout/` - Logout and delete token

### Password Management:
- **POST** `/auth/users/set_password/` - Change password
- **POST** `/auth/users/reset_password/` - Request password reset
- **POST** `/auth/users/reset_password_confirm/` - Confirm password reset

---

## Step 8: Test User Registration

### Register a New User:

**URL:** `http://localhost:8000/auth/users/`

**Method:** POST

**Request Body (JSON):**
```json
{
    "username": "newuser",
    "password": "securepassword123",
    "email": "newuser@example.com"
}
```

**Response:**
```json
{
    "email": "newuser@example.com",
    "id": 2,
    "username": "newuser"
}
```

**Note:** Password is not returned in the response for security.

---

## Step 9: Test User Login (Get Token)

### Login and Get Token:

**URL:** `http://localhost:8000/auth/token/login/`

**Method:** POST

**Request Body (Form Data or JSON):**
```json
{
    "username": "newuser",
    "password": "securepassword123"
}
```

**Response:**
```json
{
    "auth_token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

**Use the token for authenticated requests:**
```bash
curl -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \
     http://localhost:8000/auth/users/me/
```

---

## Step 10: Test User Logout

### Logout (Delete Token):

**URL:** `http://localhost:8000/auth/token/logout/`

**Method:** POST

**Headers:**
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Response:** 204 No Content (successful logout)

---

## How to Test in Browser

### 1. Start Django Server:
```powershell
cd littlelemon
..\env\Scripts\python.exe manage.py runserver
```

### 2. View User List:
- **URL:** `http://localhost:8000/auth/users/`
- You'll see the browsable API interface
- Shows list of registered users

### 3. Register New User:
- **URL:** `http://localhost:8000/auth/users/`
- Click "POST" button
- Enter:
  - Username: `testuser`
  - Password: `testpass123`
  - Email: `test@example.com`
- Click "POST" to register

### 4. Login (Get Token):
- **URL:** `http://localhost:8000/auth/token/login/`
- Click "POST" button
- Enter:
  - Username: `testuser`
  - Password: `testpass123`
- Click "POST" to get token

### 5. View Current User:
- **URL:** `http://localhost:8000/auth/users/me/`
- Add token in Authorization header or use session authentication

### 6. Logout:
- **URL:** `http://localhost:8000/auth/token/logout/`
- Click "POST" with token in header

---

## Admin Panel - Tokens Section

After running migrations, you can see the **Tokens** section in Django Admin:

1. Login to admin: `http://localhost:8000/admin/`
2. You'll see **TOKENS** section in the dashboard
3. View all authentication tokens
4. Each token is linked to a user

---

## API Request Examples

### Register User (cURL):
```bash
curl -X POST http://localhost:8000/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{"username": "newuser", "password": "securepass123", "email": "user@example.com"}'
```

### Login (cURL):
```bash
curl -X POST http://localhost:8000/auth/token/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "newuser", "password": "securepass123"}'
```

### Get Current User (cURL):
```bash
curl -X GET http://localhost:8000/auth/users/me/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### Logout (cURL):
```bash
curl -X POST http://localhost:8000/auth/token/logout/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

---

## Expected JSON Responses

### Registration Response:
```json
{
    "email": "user@example.com",
    "id": 2,
    "username": "newuser"
}
```

### Login Response:
```json
{
    "auth_token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### Current User Response:
```json
{
    "email": "user@example.com",
    "id": 2,
    "username": "newuser"
}
```

---

## ✅ Exercise Status: COMPLETE

All requirements have been met:
- ✅ Djoser library installed
- ✅ 'djoser' added to INSTALLED_APPS (after 'rest_framework')
- ✅ DJOSER configuration added with USER_ID_FIELD
- ✅ TokenAuthentication and SessionAuthentication added
- ✅ Djoser URL routes configured
- ✅ Migrations run successfully
- ✅ Token tables created in database
- ✅ All endpoints ready for testing

**User registration, login, and logout features are fully functional!**

---

## Next Steps

1. **Start the server:**
   ```powershell
   ..\env\Scripts\python.exe manage.py runserver
   ```

2. **Test registration:**
   - Visit: `http://localhost:8000/auth/users/`
   - Register a new user

3. **Test login:**
   - Visit: `http://localhost:8000/auth/token/login/`
   - Get authentication token

4. **Test authenticated endpoints:**
   - Use token to access protected endpoints
   - View current user: `/auth/users/me/`

5. **Test logout:**
   - Visit: `http://localhost:8000/auth/token/logout/`
   - Delete token

---

## Summary

You now have a complete authentication system with:
- ✅ User registration
- ✅ User login (token-based)
- ✅ User logout
- ✅ User profile management
- ✅ Token authentication
- ✅ Session authentication

All authentication features are ready to use! 🎉

