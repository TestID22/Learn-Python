import requests
from bs4 import BeautifulSoup
from multiprocessing import pool

url = 'https://ru.investing.com/crypto/currencies'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}

def getHtml(url):
    html = requests.get(url, headers=headers)
    return html.text

def getNames(html):
    soup = BeautifulSoup(html)
    tds = soup.find_all('td',class_='left bold elp name cryptoName first js-currency-name')
    names = []
    for td in tds:
        names.append(td.text)                              
    return names

#def soCollFunc(url):
#    html = getHtml(url)
#    llinks = getNames(html)

def saveText(links):
    cname = open('curname.txt', 'w')
    for link in links:
        cname.write(str(link + '\n'))
    cname.close
    

#def readcname(cname):
#    with open(cname, 'wb') as f:
#        f.read()
#        print(f.read())



def main():
    html = getHtml(url)
    links = getNames(html)
    fname = saveText(links)
    
    #with pool(2) as p:
    #      p.map(soCollFunc)

if __name__ == "__main__":
    main()