import requests
from bs4 import BeautifulSoup


url1 = 'https://www.olx.ua/'
userid = '12345'

#Эмуляция USER - Agent = с использованием словаря
headers = {
           'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
          }

r = requests.get(url1, headers = headers)
print('Статус подключения', r)

with open('parse.html', 'w')as parse:
    parse.write(str(r))