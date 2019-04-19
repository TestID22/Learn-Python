from urllib.request import urlopen
from bs4 import BeautifulSoup
#Скрапаем валютные пары
site = urlopen('https://www.finanz.ru/valyuty/v-realnom-vremeni')
soup = BeautifulSoup(site)
exchange = soup.find('table',{'class':'quote_list'}).find_all('a')
name = []
links = []

for name_cur in exchange:
    name.append(name_cur.get_text())
    if 'href' and 'title' in name_cur.attrs:
        links.append(name_cur.attrs['href'])
    
name = list(set(name))
name_ex = name[1:]

print(name_ex)
print(links)



