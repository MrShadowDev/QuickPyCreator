# QuickPyCreator

QuickPyCreator is a lightweight Python tool that runs in the background and automatically creates a `main.py` file in your current directory with a single keystroke (**Ctrl + M**). Perfect for developers who want to save time and streamline their workflow!

## Features
- Automatically creates a `main.py` file with a single keystroke (**Ctrl + M**).
- Runs in the background with a system tray icon for easy control.
- Adds itself to Windows Startup for seamless integration.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MrShadowDev/QuickPyCreator

2. Run the installation script:
- On **Windows**: Double-click `install.bat`.

3. The tool will now run automatically on startup.

## Usage
Press **Ctrl + M** to create a `main.py` file in your current directory.

Use the system tray icon to exit the application.

## Logging
All events (e.g., file creation) are logged in the `logs/file_creator_logs.txt` file with timestamps and directory information.

## TODO Checklist

### Features
- [x] Create an uninstallation script (`uninstall.bat`) to remove the tool from startup.
- [ ] Add cross-platform support (macOS and Linux).
- [ ] Allow users to customize the `main.py` template via a `config.json` file.
---

This setup is fully automated. Let me know if you need further assistance. Feel free to open an **ISSUE** or to **CONTRIBUTE**
