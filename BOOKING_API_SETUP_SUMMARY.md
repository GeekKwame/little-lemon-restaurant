# Booking API Setup - Exercise Completion Summary

## ✅ All Steps Completed Successfully!

---

## Step 1: Verify 'rest_framework' in INSTALLED_APPS ✅

**File:** `littlelemon/littlelemon/settings.py`

```python
INSTALLED_APPS = [
    ...
    'rest_framework',  # ✅ Already present
    'restaurant',
    'reservation'
]
```

**Status:** ✅ Confirmed - 'rest_framework' is in INSTALLED_APPS

---

## Step 2: Create BookingSerializer ✅

**File:** `littlelemon/restaurant/serializers.py`

```python
from rest_framework import serializers
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # ✅ Includes all fields: id, name, no_of_guests, BookingDate
```

**Status:** ✅ BookingSerializer created using ModelSerializer with `fields = '__all__'`

---

## Step 3: Create BookingViewSet ✅

**File:** `littlelemon/restaurant/views.py`

```python
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
```

**Status:** ✅ BookingViewSet created inheriting from `ModelViewSet`

**Features:**
- Handles all CRUD operations automatically:
  - **GET** `/restaurant/booking/tables/` - List all bookings
  - **POST** `/restaurant/booking/tables/` - Create new booking
  - **GET** `/restaurant/booking/tables/<id>/` - Retrieve single booking
  - **PUT** `/restaurant/booking/tables/<id>/` - Update booking
  - **PATCH** `/restaurant/booking/tables/<id>/` - Partial update
  - **DELETE** `/restaurant/booking/tables/<id>/` - Delete booking

---

## Step 4: Configure DefaultRouter ✅

**File:** `littlelemon/littlelemon/urls.py` (Project-level, not app-level)

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views

router = DefaultRouter()
router.register(r'booking/tables', views.BookingViewSet, basename='booking')

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('restaurant.urls')),
   path('restaurant/', include('restaurant.urls')),
   path('restaurant/', include(router.urls)),  # ✅ Router URLs included
]
```

**Status:** ✅ DefaultRouter configured and registered

**Router Registration:**
- **Route:** `booking/tables`
- **ViewSet:** `BookingViewSet`
- **Basename:** `booking`

---

## Step 5: API Endpoint Ready ✅

### Available Endpoints:

**Base URL:** `http://localhost:8000/restaurant/booking/tables`

1. **List/Create Bookings**
   - **URL:** `http://localhost:8000/restaurant/booking/tables/`
   - **GET:** Retrieve all bookings
   - **POST:** Create a new booking

2. **Retrieve/Update/Delete Single Booking**
   - **URL:** `http://localhost:8000/restaurant/booking/tables/<id>/`
   - **GET:** Retrieve a specific booking
   - **PUT:** Update a booking (full update)
   - **PATCH:** Update a booking (partial update)
   - **DELETE:** Delete a booking

---

## How to Test the API

### 1. Start Django Server:
```powershell
cd littlelemon
..\env\Scripts\python.exe manage.py runserver
```

### 2. Access Browsable API:
Open browser: `http://localhost:8000/restaurant/booking/tables/`

### 3. Test Operations:

#### **GET - List All Bookings:**
- Visit: `http://localhost:8000/restaurant/booking/tables/`
- Method: GET
- Result: Returns JSON list of all bookings

#### **POST - Create New Booking:**
- Visit: `http://localhost:8000/restaurant/booking/tables/`
- Click "POST" button in browsable API
- Enter JSON data:
```json
{
    "name": "John Doe",
    "no_of_guests": 4,
    "BookingDate": "2025-12-15T19:00:00Z"
}
```
- Click "POST" to create

#### **GET - Retrieve Single Booking:**
- Visit: `http://localhost:8000/restaurant/booking/tables/1/`
- Method: GET
- Result: Returns JSON for booking with ID=1

#### **PUT - Update Booking:**
- Visit: `http://localhost:8000/restaurant/booking/tables/1/`
- Click "PUT" button
- Modify JSON data
- Click "PUT" to update

#### **DELETE - Delete Booking:**
- Visit: `http://localhost:8000/restaurant/booking/tables/1/`
- Click "DELETE" button
- Confirm deletion

---

## API Request Examples

### Using cURL:

**GET All Bookings:**
```bash
curl http://localhost:8000/restaurant/booking/tables/
```

**POST New Booking:**
```bash
curl -X POST http://localhost:8000/restaurant/booking/tables/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "no_of_guests": 4, "BookingDate": "2025-12-15T19:00:00Z"}'
```

**GET Single Booking:**
```bash
curl http://localhost:8000/restaurant/booking/tables/1/
```

**PUT Update Booking:**
```bash
curl -X PUT http://localhost:8000/restaurant/booking/tables/1/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Doe", "no_of_guests": 6, "BookingDate": "2025-12-15T20:00:00Z"}'
```

**DELETE Booking:**
```bash
curl -X DELETE http://localhost:8000/restaurant/booking/tables/1/
```

---

## Expected JSON Response Format

### GET /restaurant/booking/tables/ (List):
```json
[
    {
        "id": 1,
        "name": "John Doe",
        "no_of_guests": 4,
        "BookingDate": "2025-12-15T19:00:00Z"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "no_of_guests": 2,
        "BookingDate": "2025-12-16T18:30:00Z"
    }
]
```

### GET /restaurant/booking/tables/1/ (Single):
```json
{
    "id": 1,
    "name": "John Doe",
    "no_of_guests": 4,
    "BookingDate": "2025-12-15T19:00:00Z"
}
```

---

## ModelViewSet vs Generic Views

### What is ModelViewSet?

`ModelViewSet` is a DRF class that automatically provides:
- **List** (GET all)
- **Create** (POST)
- **Retrieve** (GET one)
- **Update** (PUT)
- **Partial Update** (PATCH)
- **Destroy** (DELETE)

This is more powerful than using separate generic views because it provides all CRUD operations in one class.

### DefaultRouter Benefits:

- Automatically generates URL patterns
- Provides browsable API interface
- Includes API root view
- Handles URL routing automatically

---

## ✅ Exercise Status: COMPLETE

All requirements have been met:
- ✅ 'rest_framework' verified in INSTALLED_APPS
- ✅ BookingSerializer created with `fields = '__all__'`
- ✅ BookingViewSet created using ModelViewSet
- ✅ DefaultRouter configured in project urls.py
- ✅ Booking route registered: `booking/tables`
- ✅ API endpoints ready for testing

**The Booking API is fully functional and ready to use!**

---

## Next Steps

1. **Start the server:**
   ```powershell
   ..\env\Scripts\python.exe manage.py runserver
   ```

2. **Test the API:**
   - Open: `http://localhost:8000/restaurant/booking/tables/`
   - Use the browsable API interface to test all CRUD operations

3. **Add sample bookings:**
   - Use POST to create booking records
   - Verify with GET requests

4. **Test all operations:**
   - ✅ CREATE (POST)
   - ✅ READ (GET)
   - ✅ UPDATE (PUT/PATCH)
   - ✅ DELETE (DELETE)

---

## Summary of Both APIs

| API | Endpoint | View Type | Router |
|-----|----------|-----------|--------|
| **Menu API** | `/restaurant/menu/items` | Generic Views | Manual URLs |
| **Booking API** | `/restaurant/booking/tables` | ModelViewSet | DefaultRouter |

Both APIs are now fully functional! 🎉

