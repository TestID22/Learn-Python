import os, time
import pyautogui

#получим размер окна 
os.startfile('https://www.google.com')                                                  
x,y = pyautogui.size()
print(x,y)
#pyautogui.moveTo (0, y)
pyautogui.moveTo (500, 470, duration=2)
#выводит сообщение на экран                             
#pyautogui.alert('текст')                                                                
time.sleep(2)                                                                       
time.sleep(2)
#pyautogui.moveTo (500, 400, duration=2)         
pyautogui.click(500,470)                        
x = 0
while x < 15:   
    pyautogui.keyDown('tab')
    pyautogui.typewrite('Hello world!\n')
    x += 1
time.sleep(2)
text = "Роботы захватывают ГУГЛЕ"
pyautogui.typewrite(text, interval=0.2)
#pyautogui.alert(text=text)