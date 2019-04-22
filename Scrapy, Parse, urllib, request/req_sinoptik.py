import requests
from bs4 import BeautifulSoup
#Погода в Новогродовке Программа для частного пользования, если тебе лень 
#посмотреть в окно
def get_html(url):
    html = requests.get(url)
    return html.text

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    get_day = soup.find('p', class_='day-link').text
    get_city = soup.find('div', class_='cityName').find('h1').text
    get_temp = soup.find('p', class_='today-temp').text
    get_text = soup.find('div', class_='description').text
    
    return get_city, get_temp, get_text, get_day

def main():
    url = 'https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BD%D0%BE%D0%B2%D0%BE%D0%B3%D1%80%D0%BE%D0%B4%D0%BE%D0%B2%D0%BA%D0%B0'
    html = get_html(url) # work
    data = get_data(html)
    tabs = '\t' * 7
    print(tabs, ' Сегодня',data[3])
    print('\n' + data[0] + '\n')
    print(data[2])
    print('Температура воздуха:', data[1])
    input('\n  Нажми "Enter" для выхода.')

if __name__ == "__main__":
    main()