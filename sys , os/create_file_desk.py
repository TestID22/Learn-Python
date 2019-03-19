import os

#ищем путь к рабочему столу
desktop_file = os.path.expanduser("~/Desktop/myfile.txt")

file = open(desktop_file, 'w')