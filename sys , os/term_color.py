import os, sys
import msvcrt 
import time

# Дискотека Борно, юзаю страшный Модуль msvcrt
def autoColor():
    while True:
        time.sleep(0.1)
        os.system("color 1A")
        time.sleep(0.1)
        os.system("color 2b")
        time.sleep(0.1)
        os.system("color 3F")
        os.system("color 5B")
        os.system("color 2C")
        time.sleep(0.1)
        os.system("color 5C")
        os.system("color 8a")
        os.system("color 3A")


while True:
    change = msvcrt.getwch()

    if change == "1":
        os.system("color 1A")
        #os.system("ftp") // to do. написать скрипт для проверки версии ФТП клиента
    elif change == "2":
        os.system("color 2b")
        os.system("telnet")
    elif change == "3":
        os.system("color 9C")
    elif change == "4":
        os.system("color 4f")
    elif change == "5":
        os.system("color 8a")
    elif change == "0":
        autoColor()
    else:
        sys.exit
