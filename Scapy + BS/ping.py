from urllib.request import urlopen
from bs4 import BeautifulSoup
from termcolor import colored

numberForCheck = input("Введите номер ТТН\n")

html = urlopen("https://novaposhta.ua/ru/tracking/?cargo_number=" + numberForCheck + "&newtracking=1")
bsObj = BeautifulSoup(html)
status = bsObj.find("div", {"class":"status"})
statusStr = str(status)
print(colored(status.get_text()),"red")

input()