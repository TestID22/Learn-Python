import os, time
import pyautogui

#получим размер окна 
x,y = pyautogui.size()
print(x,y)
pyautogui.moveTo (0,y)
#выводит сообщение на экран
#pyautogui.alert('текст')
os.startfile('https://www.google.com')
time.sleep(2)
pyautogui.click(500,500)
time.sleep(2)
pyautogui.keyDown('tab')
pyautogui.typewrite('Питон')