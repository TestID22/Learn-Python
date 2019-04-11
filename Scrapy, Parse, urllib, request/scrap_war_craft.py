from urllib.request import urlopen
from bs4 import BeautifulSoup

#Тестово скрапаем первую страницу Вар Крафт Дуротан

site = urlopen('http://loveread.ec/read_book.php?id=54345&p=1')
soup = BeautifulSoup(site.read())
give_text = soup.find_all('p',{'class':'MsoNormal'})
for text in give_text:
    print(text.get_text())