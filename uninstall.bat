@echo off
echo Uninstalling QuickPyCreator...

set STARTUP_PATH=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\file_creator_startup.bat

if exist "%STARTUP_PATH%" (
    del "%STARTUP_PATH%"
    echo Removed QuickPyCreator from startup.
) else (
    echo QuickPyCreator is not in the startup folder.
)

set LOGS_FOLDER=logs

if exist "%LOGS_FOLDER%" (
    rmdir /s /q "%LOGS_FOLDER%"
    echo Deleted the logs folder.
) else (
    echo Logs folder does not exist.
)

echo Uninstallation complete! QuickPyCreator has been removed.
pause