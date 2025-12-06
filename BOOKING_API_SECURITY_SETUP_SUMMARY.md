# Booking API Security Setup - Exercise Completion Summary

## ✅ All Steps Completed Successfully!

---

## Step 1: Verify 'rest_framework.authtoken' in INSTALLED_APPS ✅

**File:** `littlelemon/littlelemon/settings.py`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',  # ✅ Already present
    'djoser',
    ...
]
```

**Status:** ✅ Confirmed - 'rest_framework.authtoken' is in INSTALLED_APPS

---

## Step 2: Import IsAuthenticated ✅

**File:** `littlelemon/restaurant/views.py`

```python
from rest_framework.permissions import IsAuthenticated  # ✅ Imported
```

**Status:** ✅ IsAuthenticated class imported

---

## Step 3: Secure BookingViewSet ✅

**File:** `littlelemon/restaurant/views.py`

```python
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  # ✅ Added
```

**Status:** ✅ BookingViewSet secured with IsAuthenticated permission

**What this means:**
- All Booking API endpoints now require authentication
- Users must provide a valid token to access booking endpoints
- Unauthenticated requests will return `401 Unauthorized`

---

## Step 4: Add obtain_auth_token View ✅

**File:** `littlelemon/littlelemon/urls.py`

```python
from rest_framework.authtoken.views import obtain_auth_token  # ✅ Imported

urlpatterns = [
    ...
    path('api-token-auth/', obtain_auth_token),  # ✅ Added
]
```

**Status:** ✅ Token authentication endpoint configured

**Endpoint:** `http://localhost:8000/api-token-auth/`

---

## Step 5: How to Get Authentication Token

### Using Browser (Browsable API):

1. **Start Django Server:**
   ```powershell
   cd littlelemon
   ..\env\Scripts\python.exe manage.py runserver
   ```

2. **Visit Token Endpoint:**
   - URL: `http://localhost:8000/api-token-auth/`
   - Method: POST
   - Content-Type: application/json

3. **Enter Credentials:**
   ```json
   {
       "username": "admin",
       "password": "admin123"
   }
   ```

4. **Response:**
   ```json
   {
       "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
   }
   ```

### Using cURL:

```bash
curl -X POST http://localhost:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

### Using Insomnia/Postman:

1. **Method:** POST
2. **URL:** `http://localhost:8000/api-token-auth/`
3. **Body (JSON):**
   ```json
   {
       "username": "admin",
       "password": "admin123"
   }
   ```
4. **Response:** Token string

---

## Step 6: Accessing Secured Booking API

### Without Token (Will Fail):
```bash
curl http://localhost:8000/restaurant/booking/tables/
```

**Response:**
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### With Token (Success):

**Using cURL:**
```bash
curl -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \
     http://localhost:8000/restaurant/booking/tables/
```

**Using Insomnia/Postman:**
1. Go to **Auth** tab
2. Select **Bearer Token** (or **Token**)
3. Enter token: `9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`
4. Send request

**Response:** List of bookings (if any exist)

---

## Secured Endpoints

All Booking API endpoints now require authentication:

| Endpoint | Method | Authentication Required |
|----------|--------|------------------------|
| `/restaurant/booking/tables/` | GET | ✅ Yes |
| `/restaurant/booking/tables/` | POST | ✅ Yes |
| `/restaurant/booking/tables/<id>/` | GET | ✅ Yes |
| `/restaurant/booking/tables/<id>/` | PUT | ✅ Yes |
| `/restaurant/booking/tables/<id>/` | PATCH | ✅ Yes |
| `/restaurant/booking/tables/<id>/` | DELETE | ✅ Yes |

---

## Token Management

### Get Token:
- **URL:** `http://localhost:8000/api-token-auth/`
- **Method:** POST
- **Body:** `{"username": "username", "password": "password"}`

### Use Token:
- **Header:** `Authorization: Token <your-token-here>`
- **Format:** `Token <token-string>` (not Bearer)

### Token in Admin Panel:
1. Login to admin: `http://localhost:8000/admin/`
2. Go to **TOKENS** section
3. View all tokens
4. Each token is linked to a user
5. Tokens can be created/deleted from admin

---

## Testing the Secured API

### Test 1: Unauthenticated Request (Should Fail)
```bash
curl http://localhost:8000/restaurant/booking/tables/
```

**Expected:** `401 Unauthorized`

### Test 2: Get Token
```bash
curl -X POST http://localhost:8000/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

**Expected:** Token string

### Test 3: Authenticated Request (Should Succeed)
```bash
curl -H "Authorization: Token YOUR_TOKEN_HERE" \
     http://localhost:8000/restaurant/booking/tables/
```

**Expected:** List of bookings or empty array

### Test 4: Create Booking (Authenticated)
```bash
curl -X POST http://localhost:8000/restaurant/booking/tables/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "no_of_guests": 4, "BookingDate": "2025-12-15T19:00:00Z"}'
```

**Expected:** Created booking object

---

## Authentication Header Format

**Important:** Use `Token` (not `Bearer`) for DRF token authentication:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

**Not:**
```
Authorization: Bearer 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b  ❌
```

---

## Complete API Flow

1. **Register User** (Optional):
   - POST `/auth/users/`
   - Create new user account

2. **Get Token**:
   - POST `/api-token-auth/`
   - Provide username and password
   - Receive token

3. **Access Secured Endpoints**:
   - Include token in Authorization header
   - Access Booking API endpoints

4. **Create/Manage Bookings**:
   - Use authenticated requests
   - All CRUD operations require token

---

## ✅ Exercise Status: COMPLETE

All requirements have been met:
- ✅ 'rest_framework.authtoken' verified in INSTALLED_APPS
- ✅ IsAuthenticated imported
- ✅ BookingViewSet secured with permission_classes
- ✅ obtain_auth_token view added to URLs
- ✅ Token authentication endpoint ready
- ✅ Booking API now requires authentication

**The Booking API is now secured with token-based authentication!**

---

## Security Summary

| Component | Status |
|-----------|--------|
| **Token Authentication** | ✅ Enabled |
| **Booking API Security** | ✅ Secured |
| **Token Endpoint** | ✅ Available |
| **Permission Classes** | ✅ IsAuthenticated |
| **Unauthenticated Access** | ❌ Blocked |

---

## Next Steps

1. **Start the server:**
   ```powershell
   ..\env\Scripts\python.exe manage.py runserver
   ```

2. **Get authentication token:**
   - Visit: `http://localhost:8000/api-token-auth/`
   - POST with username/password

3. **Test secured endpoints:**
   - Use token in Authorization header
   - Access Booking API

4. **Verify security:**
   - Try accessing without token (should fail)
   - Try accessing with token (should succeed)

---

## Important Notes

- **Token Format:** Use `Token <token>` in Authorization header (not Bearer)
- **Token Persistence:** Tokens persist until deleted or user is deleted
- **Token Security:** Keep tokens secure, don't expose in client-side code
- **Multiple Tokens:** Each user can have one token (new token replaces old one)

Your Booking API is now fully secured! 🔒

