@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  start "NOVA Server" cmd /k "py -3 nova_server.py"
  goto launch
)
where python >nul 2>nul
if %errorlevel%==0 (
  start "NOVA Server" cmd /k "python nova_server.py"
  goto launch
)
echo Python 3 was not found. Install Python 3 from python.org if permitted,
echo or open index.html for a basic interface preview (AI proxy will not work).
pause
exit /b
:launch
timeout /t 2 /nobreak >nul
start "" http://127.0.0.1:8000
exit /b
