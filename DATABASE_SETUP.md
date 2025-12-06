# Database Setup Guide for Little Lemon Restaurant

## Quick Answer
**You have 3 options:**
1. **SQLite** (Easiest - No installation needed) ✅ Recommended for development
2. **MySQL** (Install MySQL Server on your laptop)
3. **PostgreSQL** (Install PostgreSQL on your laptop)

---

## Option 1: SQLite (Recommended for Development) ⭐

**Pros:**
- ✅ No installation needed
- ✅ Already included with Python
- ✅ Perfect for development
- ✅ Single file database (easy to backup)

**Setup:**
Just change your `settings.py` to use SQLite:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**No additional steps needed!**

---

## Option 2: MySQL (If you need MySQL)

### Step 1: Install MySQL Server

**Download MySQL:**
1. Go to: https://dev.mysql.com/downloads/installer/
2. Download "MySQL Installer for Windows"
3. Choose "Full" or "Developer Default" installation
4. During installation, set a root password (remember this!)

**Or use MySQL via XAMPP (Easier):**
1. Download XAMPP: https://www.apachefriends.org/
2. Install XAMPP
3. Start MySQL from XAMPP Control Panel

### Step 2: Create Database

Open MySQL Command Line or MySQL Workbench and run:
```sql
CREATE DATABASE littlelemon_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### Step 3: Install Python MySQL Client

In your virtual environment:
```powershell
# Activate virtual environment first
..\env\Scripts\Activate.ps1

# Install mysqlclient
pip install mysqlclient
```

**Note:** If `mysqlclient` fails to install, use:
```powershell
pip install pymysql
```

### Step 4: Update settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon_db',           # Your database name
        'USER': 'root',                      # Your MySQL username
        'PASSWORD': 'your_mysql_password',   # Your MySQL password
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

### Step 5: Run Migrations

```powershell
python manage.py migrate
```

---

## Option 3: PostgreSQL (Alternative to MySQL)

### Step 1: Install PostgreSQL

1. Download from: https://www.postgresql.org/download/windows/
2. Run the installer
3. Set a password for the `postgres` user (remember this!)

### Step 2: Create Database

Open pgAdmin or psql and run:
```sql
CREATE DATABASE littlelemon_db;
```

### Step 3: Install Python PostgreSQL Client

```powershell
pip install psycopg2-binary
```

### Step 4: Update settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'littlelemon_db',
        'USER': 'postgres',
        'PASSWORD': 'your_postgres_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

---

## Option 4: Cloud Database (No Local Installation)

**Free Cloud Options:**
- **ElephantSQL** (PostgreSQL): https://www.elephantsql.com/
- **PlanetScale** (MySQL): https://planetscale.com/
- **Railway** (PostgreSQL): https://railway.app/

**Steps:**
1. Sign up for a free account
2. Create a database
3. Get connection details (host, port, username, password)
4. Update `settings.py` with cloud credentials

---

## Which Should You Choose?

| Use Case | Recommended Database |
|----------|---------------------|
| Learning/Development | **SQLite** ✅ |
| Small Project | **SQLite** ✅ |
| Production (Small) | **PostgreSQL** or **MySQL** |
| Production (Large) | **PostgreSQL** or **MySQL** |
| Team Project | **PostgreSQL** or **MySQL** |

---

## Current Status

Your project is currently configured for **MySQL** but the database might not be set up yet.

**Quick Fix:** Switch to SQLite for now (no installation needed):
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

