import pyautogui
import time

time.sleep(1)
x = 500
y = 500
#Отключаем спасалку для юзеров
pyautogui.FAILSAFE = False

print('Зря ты меня запустил')
pyautogui.typewrite('Hello world!',2)
while True:
    if x > 0:
        pyautogui.moveTo(x,y, 1)
    