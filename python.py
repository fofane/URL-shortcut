import keyboard
import subprocess
import time

# Path to Brave browser executable
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Update with your Brave path

# Define key-button mapping for each website
key_url_map = {
    'f2': 'https://classroom.btu.edu.ge/ge/student/me/course/scores/5/42',
    'f3': 'https://classroom.btu.edu.ge/ge/student/me/course/groups/536/43',
    'f4': 'https://classroom.btu.edu.ge/ge/student/me/course/index/8',
    'f5': 'https://classroom.btu.edu.ge/ge/student/me/course/index/666',
    'f6': 'https://classroom.btu.edu.ge/ge/student/me/course/index/67',
    'f7': 'https://classroom.btu.edu.ge/ge/student/me/course/index/6'
}

# Function to open URL in Brave using subprocess
def open_in_brave(url):
    subprocess.run([brave_path, url])

# Wait for a key press and open the corresponding URL in Brave
while True:
    for key, url in key_url_map.items():
        if keyboard.is_pressed(key):
            open_in_brave(url)
            print(f"Opening {url} in Brave...")
            while keyboard.is_pressed(key):  # Wait until the key is released
                time.sleep(0.1)  # Prevent high CPU usage
            break

