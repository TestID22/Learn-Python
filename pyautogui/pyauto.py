import pyautogui
import time

time.sleep(1)
x = 500
y = 500
#Отключаем спасалку для юзеров
pyautogui.FAILSAFE = False
def start():
    print('Зря ты меня запустил')
    while True:
        if x > 0:
            pyautogui.moveTo(x,y, 1)

start()
if __name__ == "__main__":
    start()