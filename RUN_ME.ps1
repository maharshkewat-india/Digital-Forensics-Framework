# PowerShell one-click launcher
# Right-click and "Run with PowerShell" to execute

Write-Host "`n"
Write-Host "╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║         DIGITAL EVIDENCE FRAMEWORK - MASTER LAUNCHER           ║" -ForegroundColor Cyan
Write-Host "║                   Run Everything With One Click!               ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host "`n"

# Set execution policy for this session
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force

# Get script directory
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

# Check if LAUNCHER.py exists
if (-Not (Test-Path "LAUNCHER.py")) {
    Write-Host "❌ Error: LAUNCHER.py not found!" -ForegroundColor Red
    Write-Host "Make sure you're in the correct folder." -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Run the launcher
Write-Host "Starting launcher..." -ForegroundColor Green
python LAUNCHER.py

# Check if successful
if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ Launcher completed successfully!" -ForegroundColor Green
} else {
    Write-Host "`n⚠️  Launcher closed with code: $LASTEXITCODE" -ForegroundColor Yellow
}

Write-Host "`nPress Enter to close this window..." -ForegroundColor Gray
Read-Host
