from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        soup = BeautifulSoup(html.read())
        title = soup.find('title')
        
    except AttributeError as e:
        return None 
    return title

title = get_title('https://mrrobot.fandom.com/')
if title == None:
    print('Заголовок не найден, но сайт есть...=(')
else:
    print(title)
