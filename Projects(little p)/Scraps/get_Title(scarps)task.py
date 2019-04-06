from urllib.request import urlopen
from bs4 import BeautifulSoup

site = urlopen('file:///E:/Projects/Code/Alex-site.html')
soup = BeautifulSoup(site.read())
get_title = soup.find('title')
print(get_title)