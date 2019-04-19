import requests
from bs4 import BeautifulSoup
#Погода в Новогродовке Программа для частного пользования, если тебе лень 
#посмотреть в окно
def get_html(url):
    html = requests.get(url)
    return html.text

def get_data(html):
    soup = BeautifulSoup(html)
    get_city = soup.find('div', class_='cityName').find('h1').text
    get_temp = soup.find('p', class_='today-temp').text
    get_text = soup.find('div', class_='description').text
    
    return get_city, get_temp, get_text

def main():
    url = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BD%D0%BE%D0%B2%D0%BE%D0%B3%D1%80%D0%BE%D0%B4%D0%BE%D0%B2%D0%BA%D0%B0'
    html = get_html(url) # work
    data = get_data(html)
    print('\n' + data[0] + '\n')
    print(data[2])
    print('Температура воздуха:', data[1])
    input('Нажми "Enter" для выхода.')

if __name__ == "__main__":
    main()