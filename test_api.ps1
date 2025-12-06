# Little Lemon Restaurant API Testing Script

Write-Host "=== Testing Little Lemon Restaurant API ===" -ForegroundColor Green
Write-Host ""

# Test 1: Homepage
Write-Host "1. Testing Homepage..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/" -Method GET -UseBasicParsing
    Write-Host "   ✅ Homepage: Status $($response.StatusCode)" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Homepage: Failed - $($_.Exception.Message)" -ForegroundColor Red
}

# Test 2: Menu API - List Items
Write-Host "2. Testing Menu API (GET)..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/restaurant/menu/items" -Method GET -UseBasicParsing
    Write-Host "   ✅ Menu API: Status $($response.StatusCode)" -ForegroundColor Green
    $content = $response.Content | ConvertFrom-Json
    Write-Host "   📋 Menu Items Count: $($content.Count)" -ForegroundColor Cyan
} catch {
    Write-Host "   ❌ Menu API: Failed - $($_.Exception.Message)" -ForegroundColor Red
}

# Test 3: Get Authentication Token
Write-Host "3. Testing Token Authentication..." -ForegroundColor Yellow
$token = $null
try {
    $body = @{
        username = "admin"
        password = "admin123"
    } | ConvertTo-Json
    
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/api-token-auth/" -Method POST -Body $body -ContentType "application/json" -UseBasicParsing
    $tokenData = $response.Content | ConvertFrom-Json
    $token = $tokenData.token
    Write-Host "   ✅ Token Obtained: $($token.Substring(0, 20))..." -ForegroundColor Green
} catch {
    Write-Host "   ❌ Token Authentication: Failed - $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "   💡 Make sure you have a user with username 'admin' and password 'admin123'" -ForegroundColor Yellow
}

# Test 4: Booking API - Without Token (Should Fail)
Write-Host "4. Testing Booking API (Without Token - Should Fail)..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/restaurant/booking/tables/" -Method GET -UseBasicParsing
    Write-Host "   ⚠️  Booking API: Unexpected success (should require auth)" -ForegroundColor Yellow
} catch {
    if ($_.Exception.Response.StatusCode -eq 401) {
        Write-Host "   ✅ Booking API: Correctly requires authentication (401)" -ForegroundColor Green
    } else {
        Write-Host "   ❌ Booking API: Error - $($_.Exception.Message)" -ForegroundColor Red
    }
}

# Test 5: Booking API - With Token (Should Succeed)
if ($token) {
    Write-Host "5. Testing Booking API (With Token - Should Succeed)..." -ForegroundColor Yellow
    try {
        $headers = @{
            "Authorization" = "Token $token"
        }
        $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/restaurant/booking/tables/" -Method GET -Headers $headers -UseBasicParsing
        Write-Host "   ✅ Booking API: Status $($response.StatusCode)" -ForegroundColor Green
        $content = $response.Content | ConvertFrom-Json
        Write-Host "   📋 Bookings Count: $($content.Count)" -ForegroundColor Cyan
    } catch {
        Write-Host "   ❌ Booking API: Failed - $($_.Exception.Message)" -ForegroundColor Red
    }
}

# Test 6: User Registration
Write-Host "6. Testing User Registration..." -ForegroundColor Yellow
try {
    $body = @{
        username = "testuser_$(Get-Random)"
        password = "testpass123"
        email = "test@example.com"
    } | ConvertTo-Json
    
    $response = Invoke-WebRequest -Uri "http://127.0.0.1:8000/auth/users/" -Method POST -Body $body -ContentType "application/json" -UseBasicParsing
    Write-Host "   ✅ User Registration: Status $($response.StatusCode)" -ForegroundColor Green
    $userData = $response.Content | ConvertFrom-Json
    Write-Host "   👤 User Created: $($userData.username) (ID: $($userData.id))" -ForegroundColor Cyan
} catch {
    Write-Host "   ❌ User Registration: Failed - $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
Write-Host "=== Testing Complete ===" -ForegroundColor Green
Write-Host ""
Write-Host "🌐 Open these URLs in your browser:" -ForegroundColor Cyan
Write-Host "   Homepage: http://127.0.0.1:8000/" -ForegroundColor White
Write-Host "   Admin: http://127.0.0.1:8000/admin/" -ForegroundColor White
Write-Host "   Menu API: http://127.0.0.1:8000/restaurant/menu/items" -ForegroundColor White
Write-Host "   Booking API: http://127.0.0.1:8000/restaurant/booking/tables/" -ForegroundColor White
Write-Host "   Token Auth: http://127.0.0.1:8000/api-token-auth/" -ForegroundColor White
Write-Host "   User Registration: http://127.0.0.1:8000/auth/users/" -ForegroundColor White

