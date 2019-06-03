import os, sys
import msvcrt 

# Дискотека Борно, юзаю страшный Модуль msvcrt
def getColor():
    print("1- Color")
    print("2- Color ")
    print("3- Color")
    print("4- Color")

while True:
    change = msvcrt.getwch()

    if change == "1":
        os.system("color 1A")
        
    elif change == "2":
        os.system("color 2b")
    elif change == "3":
        os.system("color 9C")
    elif change == "4":
        os.system("color 4f")
    elif change == "5":
        os.system("color 8a")
    else:
        sys.exit
