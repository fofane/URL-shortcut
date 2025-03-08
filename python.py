import keyboard
import subprocess
import time

# Path to Brave browser executable
path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Update with your path

# Define key-button mapping for each website
key_url_map = {
    'f1': 'https://www.example1.com',
    'f2': 'https://www.example2.com',
    'f3': 'https://www.example3.com',
    'f4': 'https://www.example4.com',
    'f5': 'https://www.example5.com',
    'f6': 'https://www.example6.com'
}

# Function to open URL in Brave using subprocess
def open_in_brave(url):
    subprocess.run([path, url])

# Wait for a key press and open the corresponding URL in Brave
while True:
    for key, url in key_url_map.items():
        if keyboard.is_pressed(key):
            open_in_brave(url)
            print(f"Opening {url} in Brave...")
            while keyboard.is_pressed(key):  # Wait until the key is released
                time.sleep(0.1)  # Prevent high CPU usage
            break

