@echo off
echo Installing QuickPyCreator...

pip install keyboard pystray pillow

set SCRIPT_PATH=%~dp0code.py
set STARTUP_PATH=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\code.bat

echo Adding to startup...
echo @echo off > "%STARTUP_PATH%"
echo pythonw "%SCRIPT_PATH%" >> "%STARTUP_PATH%"

echo Installation complete! QuickPyCreator will now run on startup.
pause