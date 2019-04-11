import urllib.request
from bs4 import BeautifulSoup

headers = {'User-Agent':\
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) \
            AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4'}
site = urllib.request.Request('https://2ip.ru/', headers = headers)
html = urllib.request.urlopen(site)
soup = BeautifulSoup(html.read())

find_my_os = soup.find('table', id='main-info-block')\
                        .find_all('span',{'class':'ip-info-entry__value'})

find_my_browser = soup.find('table', id='main-info-block').find_all('span',{'class':'ip-info-entry__value'})
print('Ваш Браузур:', find_my_browser[2].text + '\nВаша операционная система:',find_my_os[1].text)
input('Данные Любезно предоставленные сервисом 2ip.ru')


