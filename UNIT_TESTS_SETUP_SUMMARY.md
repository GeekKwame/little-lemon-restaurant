# Unit Tests Setup Summary

## ✅ Exercise Completed: Adding Unit Tests

This document summarizes the unit tests implementation for the Little Lemon Restaurant application.

---

## 📋 Steps Completed

### Step 1: Delete Existing test.py File
- ✅ Deleted `littlelemon/restaurant/tests.py` (empty test file)

### Step 2: Create Tests Folder
- ✅ Created `tests/` folder in the project root (`littlelemon/tests/`)
- ✅ Created `tests/__init__.py` to make it a Python package

### Step 3: Verify Menu Model __str__ Method
- ✅ Confirmed `Menu` model already has `__str__()` method:
  ```python
  def __str__(self):
      return f'{self.title} : {str(self.price)}'
  ```

### Step 4: Create test_models.py
- ✅ Created `littlelemon/tests/test_models.py`
- ✅ Implemented `MenuTest` class with `test_get_item()` method
- ✅ Tests the string representation of Menu model instances

### Step 5: Create test_views.py
- ✅ Created `littlelemon/tests/test_views.py`
- ✅ Implemented `MenuViewTest` class with:
  - `setUp()` method to create test Menu instances
  - `test_getall()` method to test the Menu API endpoint

---

## 📁 File Structure

```
littlelemon/
├── manage.py
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   └── test_views.py
├── restaurant/
│   ├── models.py (Menu model with __str__ method)
│   ├── views.py (MenuItemView)
│   └── serializers.py (MenuSerializer)
└── ...
```

---

## 🧪 Test Files

### test_models.py

```python
from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")
```

**Purpose:** Tests the `__str__()` method of the Menu model to ensure it returns the correct string representation.

---

### test_views.py

```python
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=15.99, inventory=50)
        Menu.objects.create(title="Burger", price=12.50, inventory=75)
        
        # Initialize API client
        self.client = APIClient()
    
    def test_getall(self):
        # Retrieve all Menu objects
        url = '/restaurant/menu/items'
        response = self.client.get(url)
        
        # Check if the response status is OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Get all Menu objects and serialize them
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        
        # Check if the serialized data equals the response
        self.assertEqual(response.data, serializer.data)
```

**Purpose:** 
- Tests the Menu API endpoint (`/restaurant/menu/items`)
- Verifies that all Menu items are correctly retrieved and serialized
- Ensures the API response matches the expected serialized data

---

## ✅ Test Results

### Running Tests

```bash
python manage.py test
```

### Output

```
Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.043s

OK
Destroying test database for alias 'default'...
```

### Detailed Test Output (with -v 2)

```
test_get_item (tests.test_models.MenuTest.test_get_item) ... ok
test_getall (tests.test_views.MenuViewTest.test_getall) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.039s

OK
```

---

## 🎯 Test Coverage

### Model Tests
- ✅ **MenuTest.test_get_item**: Verifies `__str__()` method returns correct format

### View Tests
- ✅ **MenuViewTest.test_getall**: Verifies Menu API endpoint returns all items correctly

---

## 📝 Key Testing Concepts

### 1. Django TestCase
- Django's test framework uses Python's `unittest` package
- `TestCase` provides database isolation (creates test database)
- Each test method runs in isolation

### 2. setUp() Method
- Called before each test method
- Used to set up test data
- In our case, creates Menu instances for testing

### 3. APIClient
- DRF's test client for making API requests
- Simulates HTTP requests without running a server
- Returns response objects with `.data` attribute

### 4. Assertions
- `assertEqual()`: Compares two values for equality
- `assertEqual(response.status_code, status.HTTP_200_OK)`: Checks HTTP status
- `assertEqual(response.data, serializer.data)`: Compares serialized data

---

## 🔍 What the Tests Verify

### Model Test (test_models.py)
1. Creates a Menu instance with specific data
2. Checks that `str(item)` returns `"IceCream : 80"`
3. Validates the `__str__()` method implementation

### View Test (test_views.py)
1. Creates multiple Menu instances in `setUp()`
2. Makes GET request to `/restaurant/menu/items`
3. Verifies HTTP 200 OK response
4. Compares API response with serialized data
5. Ensures all Menu items are returned correctly

---

## 🚀 Running Tests

### Run All Tests
```bash
python manage.py test
```

### Run Specific Test File
```bash
python manage.py test tests.test_models
python manage.py test tests.test_views
```

### Run Specific Test Class
```bash
python manage.py test tests.test_models.MenuTest
python manage.py test tests.test_views.MenuViewTest
```

### Run Specific Test Method
```bash
python manage.py test tests.test_models.MenuTest.test_get_item
python manage.py test tests.test_views.MenuViewTest.test_getall
```

### Verbose Output
```bash
python manage.py test -v 2
```

---

## ✅ Exercise Completion Checklist

- [x] Deleted existing `test.py` file in restaurant app
- [x] Created `tests/` folder in project root
- [x] Verified Menu model has `__str__()` method
- [x] Created `test_models.py` with `MenuTest` class
- [x] Created `test_views.py` with `MenuViewTest` class
- [x] Implemented `test_get_item()` method
- [x] Implemented `setUp()` method in `MenuViewTest`
- [x] Implemented `test_getall()` method
- [x] Ran tests successfully - all tests pass ✅

---

## 📚 Additional Notes

### Test Database
- Django automatically creates a separate test database
- Test database is destroyed after tests complete
- No impact on your development database

### Test Isolation
- Each test runs in isolation
- Database is reset between tests
- `setUp()` runs before each test method

### Best Practices
- ✅ Tests are in a separate `tests/` folder
- ✅ Tests use descriptive names
- ✅ Tests verify both status codes and data
- ✅ Tests use serializers for consistency
- ✅ Tests are independent and can run in any order

---

## 🎉 Summary

All unit tests have been successfully implemented and are passing! The tests verify:

1. **Model Behavior**: Menu model's `__str__()` method works correctly
2. **API Functionality**: Menu API endpoint returns all items with correct serialization

The application now has proper test coverage for the Menu model and Menu API endpoint.

---

**Status:** ✅ **All Tests Passing**

**Date:** December 6, 2025

