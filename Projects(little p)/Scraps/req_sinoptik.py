import requests
from bs4 import BeautifulSoup

html = requests.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BD%D0%BE%D0%B2%D0%BE%D0%B3%D1%80%D0%BE%D0%B4%D0%BE%D0%B2%D0%BA%D0%B0')
soup = BeautifulSoup(html.text)

get_city = soup.find('div', class_='cityName').find('h1').text
get_temp = soup.find('tr', class_='temperature').find('td', class_='p5').text
get_text = soup.find('div', class_='description').text
print(get_city)
print(get_text, ' На данный момент температура воздуха составит:' ,get_temp)