# Reload PATH environment variable in current PowerShell session
$env:PATH = [Environment]::GetEnvironmentVariable("PATH", "User") + ";" + [Environment]::GetEnvironmentVariable("PATH", "Machine")
Write-Host "✅ PATH reloaded. MySQL should now work." -ForegroundColor Green
mysql --version

