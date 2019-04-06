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
        title = html.head.title
    except AttributeError as e:
        return None 
    return title

title = get_title('https://scrap.tf/')
if title == None:
    print('Заголовок не найден, но сайт есть...=(')
else:
    print(title)