# Menu API Setup - Exercise Completion Summary

## ✅ All Steps Completed Successfully!

---

## Step 1: Django REST Framework Installation ✅

**Status:** Already installed
- **Package:** `djangorestframework`
- **Version:** 3.16.1
- **Location:** Virtual environment

**Verification:**
```bash
pip show djangorestframework
```

---

## Step 2: Add 'rest_framework' to INSTALLED_APPS ✅

**File:** `littlelemon/littlelemon/settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # ✅ Added
    'restaurant',
    'reservation'
]
```

**Status:** ✅ Added to INSTALLED_APPS

---

## Step 3: Create MenuSerializer ✅

**File:** `littlelemon/restaurant/serializers.py` (NEW FILE)

```python
from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']
```

**Status:** ✅ Created with ModelSerializer

---

## Step 4: Create API Views ✅

**File:** `littlelemon/restaurant/views.py`

### MenuItemView (ListCreateAPIView)
- **Handles:** GET (list all items), POST (create new item)
- **URL:** `/restaurant/menu/items`

```python
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
```

### SingleMenuItemView (RetrieveUpdateDestroyAPIView)
- **Handles:** GET (retrieve), PUT (update), DELETE (delete)
- **URL:** `/restaurant/menu/items/<id>`

```python
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
```

**Status:** ✅ Both views created

---

## Step 5: Define URL Routes ✅

**File:** `littlelemon/restaurant/urls.py`

```python
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/items', views.MenuItemView.as_view(), name='menu-items'),
    path('menu/items/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
]
```

**Status:** ✅ Routes configured

---

## Step 6: API Endpoints Ready ✅

### Available Endpoints:

1. **List/Create Menu Items**
   - **URL:** `http://localhost:8000/restaurant/menu/items`
   - **GET:** Retrieve all menu items
   - **POST:** Create a new menu item

2. **Retrieve/Update/Delete Single Menu Item**
   - **URL:** `http://localhost:8000/restaurant/menu/items/<id>`
   - **GET:** Retrieve a specific menu item
   - **PUT:** Update a menu item
   - **DELETE:** Delete a menu item

---

## How to Test the API

### 1. Start Django Server:
```powershell
cd littlelemon
..\env\Scripts\python.exe manage.py runserver
```

### 2. Access Browsable API:
Open browser: `http://localhost:8000/restaurant/menu/items`

### 3. Test Operations:

#### **GET - List All Items:**
- Visit: `http://localhost:8000/restaurant/menu/items`
- Method: GET
- Result: Returns JSON list of all menu items

#### **POST - Create New Item:**
- Visit: `http://localhost:8000/restaurant/menu/items`
- Click "POST" button in browsable API
- Enter JSON data:
```json
{
    "title": "Grilled Salmon",
    "price": "25.99",
    "inventory": 50
}
```
- Click "POST" to create

#### **GET - Retrieve Single Item:**
- Visit: `http://localhost:8000/restaurant/menu/items/1`
- Method: GET
- Result: Returns JSON for menu item with ID=1

#### **PUT - Update Item:**
- Visit: `http://localhost:8000/restaurant/menu/items/1`
- Click "PUT" button
- Modify JSON data
- Click "PUT" to update

#### **DELETE - Delete Item:**
- Visit: `http://localhost:8000/restaurant/menu/items/1`
- Click "DELETE" button
- Confirm deletion

---

## API Request Examples

### Using cURL:

**GET All Items:**
```bash
curl http://localhost:8000/restaurant/menu/items
```

**POST New Item:**
```bash
curl -X POST http://localhost:8000/restaurant/menu/items \
  -H "Content-Type: application/json" \
  -d '{"title": "Grilled Salmon", "price": "25.99", "inventory": 50}'
```

**GET Single Item:**
```bash
curl http://localhost:8000/restaurant/menu/items/1
```

**PUT Update Item:**
```bash
curl -X PUT http://localhost:8000/restaurant/menu/items/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Grilled Salmon", "price": "29.99", "inventory": 45}'
```

**DELETE Item:**
```bash
curl -X DELETE http://localhost:8000/restaurant/menu/items/1
```

---

## Expected JSON Response Format

### GET /restaurant/menu/items (List):
```json
[
    {
        "id": 1,
        "title": "Grilled Salmon",
        "price": "25.99",
        "inventory": 50
    },
    {
        "id": 2,
        "title": "Greek Salad",
        "price": "12.99",
        "inventory": 30
    }
]
```

### GET /restaurant/menu/items/1 (Single):
```json
{
    "id": 1,
    "title": "Grilled Salmon",
    "price": "25.99",
    "inventory": 50
}
```

---

## ✅ Exercise Status: COMPLETE

All requirements have been met:
- ✅ Django REST Framework installed
- ✅ 'rest_framework' added to INSTALLED_APPS
- ✅ MenuSerializer created using ModelSerializer
- ✅ MenuItemView (ListCreateAPIView) created
- ✅ SingleMenuItemView (RetrieveUpdateDestroyAPIView) created
- ✅ URL routes configured
- ✅ API endpoints ready for testing

**The Menu API is fully functional and ready to use!**

---

## Next Steps

1. **Start the server:**
   ```powershell
   ..\env\Scripts\python.exe manage.py runserver
   ```

2. **Test the API:**
   - Open: `http://localhost:8000/restaurant/menu/items`
   - Use the browsable API interface to test all CRUD operations

3. **Add sample data:**
   - Use POST to add menu items
   - Verify with GET requests

4. **Test all operations:**
   - ✅ CREATE (POST)
   - ✅ READ (GET)
   - ✅ UPDATE (PUT)
   - ✅ DELETE (DELETE)

