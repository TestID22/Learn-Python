
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen ('http://girnyk.dn.ua/news/na_shakhte_v_novogrodovke_gornjaki_objavili_zabastovku/2019-02-18-13629')
beautifulsoup_object = BeautifulSoup(html.read())
print(beautifulsoup_object)
input()