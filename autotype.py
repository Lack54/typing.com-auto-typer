from PIL import Image, ImageGrab
import pytesseract
import pyautogui
import time
import keyboard  # Import the keyboard module for handling key events
import random
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  

time.sleep(2)

bbox = (795, 242, 1747, 512)


def capture_and_type():
    # Take a screenshot
    screenshot = ImageGrab.grab(bbox=bbox)
    

    extracted_text = pytesseract.image_to_string(screenshot)

    # Type the extracted text using PyAutoGUI
    for char in extracted_text:
        pyautogui.write(char)

        time.sleep(random.uniform(0.02, 0.04))
        





while True:
    capture_and_type()
