import os
import time
import keyboard
from threading import Thread
import pystray
from PIL import Image
import subprocess
from datetime import datetime

if not os.path.exists("logs"):
    os.makedirs("logs")

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    with open(os.path.join("logs", "file_creator_logs.txt"), "a") as log_file:
        log_file.write(log_entry)

def create_main_py():
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, "main.py")
    
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("# This is your new main.py file\n")
            file.write("print('Hello, World!')\n")
        log_event(f"Created main.py at: {file_path}")
    else:
        log_event(f"main.py already exists in: {current_directory}")

def listen_for_shortcut():
    while True:
        if keyboard.is_pressed('ctrl+m'):
            create_main_py()
            time.sleep(1) 

def exit_app(icon):
    icon.stop()
    os._exit(0)

def uninstall_app(icon):
    icon.stop()
    log_event("Uninstalling QuickPyCreator...")
    subprocess.run(["uninstall.bat"], shell=True)
    os._exit(0)

def create_tray_icon():
    image = Image.open("icon.png")
    menu = pystray.Menu(
        pystray.MenuItem("Exit", exit_app),
        pystray.MenuItem("Uninstall", uninstall_app)
    )
    icon = pystray.Icon("file_creator", image, "File Creator Service", menu)
    icon.run()

def add_to_startup():
    script_path = os.path.abspath(__file__)
    bat_path = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "code.bat")
    
    with open(bat_path, "w") as bat_file:
        bat_file.write(f'@echo off\npythonw "{script_path}"')
    log_event(f"Added to startup: {bat_path}")

def main():
    if not os.path.exists(os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "code.bat")):
        add_to_startup()
    
    time.sleep(300)
    
    listener_thread = Thread(target=listen_for_shortcut, daemon=True)
    listener_thread.start()
    
    tray_thread = Thread(target=create_tray_icon, daemon=True)
    tray_thread.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        log_event("Application exited by user.")
        print("Exiting...")

if __name__ == "__main__":
    main()