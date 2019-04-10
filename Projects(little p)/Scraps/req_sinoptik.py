import requests
from bs4 import BeautifulSoup

html = requests.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BD%D0%BE%D0%B2%D0%BE%D0%B3%D1%80%D0%BE%D0%B4%D0%BE%D0%B2%D0%BA%D0%B0')
soup = BeautifulSoup(html.text)
get_t = soup.find('table', class_='weatherDetails').find_all('tr', class_='temperature')

print(get_t)