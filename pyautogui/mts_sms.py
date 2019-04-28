import pyautogui, os, time

os.startfile('https://www.vodafone.ua/ru#sms-form')
time.sleep(10)
pyautogui.moveTo(555, 666)
time.sleep(2)
pyautogui.click()