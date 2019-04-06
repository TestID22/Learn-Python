from urllib.request import urlopen
from bs4 import BeautifulSoup

site = urlopen('https://mrrobot.fandom.com/')
soup = BeautifulSoup(site.read())
get_title = soup.find('title')
print(get_title)