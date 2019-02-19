import pyautogui
import time

time.sleep(1)
x = 500
pyautogui.FAILSAFE = False
print('Петушок')
while True:
    
    pyautogui.moveTo(x,176, 1)
    x += 10
    