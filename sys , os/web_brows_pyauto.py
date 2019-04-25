import os
import pyautogui
import time

os.startfile('https://www.google.com')
time.sleep(3)
pyautogui.mouseDown(500,454)
pyautogui.typewrite('septemberEatMe')
pyautogui.hotkey('Enter')
time.sleep(3)
pyautogui.mouseDown(175, 320)
pyautogui.hotkey('Enter')