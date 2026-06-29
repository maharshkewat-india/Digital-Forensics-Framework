@echo off
REM Digital Evidence Framework - ONE CLICK LAUNCHER
REM This batch file runs the master launcher

title Digital Evidence Framework - Master Launcher
color 0A

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║         DIGITAL EVIDENCE FRAMEWORK - MASTER LAUNCHER           ║
echo ║                   Starting in 2 seconds...                     ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Get the directory where this batch file is located
setlocal enabledelayedexpansion
cd /d "%~dp0"

REM Wait 2 seconds
timeout /t 2 /nobreak

REM Run the Python launcher
python LAUNCHER.py

REM If Python launcher closes, show a message
if errorlevel 1 (
    echo.
    echo ╔════════════════════════════════════════════════════════════════╗
    echo ║                        ERROR                                   ║
    echo ║   Python launcher failed. Make sure Python is installed.       ║
    echo ║                                                                ║
    echo ║   Troubleshooting:                                             ║
    echo ║   1. Check Python is installed: python --version               ║
    echo ║   2. Run launcher from project folder                          ║
    echo ║   3. Try running LAUNCHER.py directly                          ║
    echo ╚════════════════════════════════════════════════════════════════╝
    echo.
    pause
)

REM Keep window open for a moment before closing
echo.
pause
