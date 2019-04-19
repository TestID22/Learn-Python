import requests
from bs4 import BeautifulSoup

def get_html(url):
    html = requests.get(url)
    return html.text #возвращает страшно некрасивый HTML 

def get_name_links(html):
    soup = BeautifulSoup(html)
    find_table = soup.findAll('div', class_="SortTable-col SortTable-data")
    links = []
    for link in find_table:
        a = link.find('a', class_='Link').get('href')
        full_url = 'https://worldofwarcraft.com' + a
        links.append(full_url)
    return links
   
def get_data(html):
    soup = BeautifulSoup(html)
    find_name = soup.find('a', class_='Link CharacterHeader-name').text 
    find_class = soup.find('div', class_='CharacterHeader-detail').text
    
    return find_name + find_class

def main():
    url = 'https://worldofwarcraft.com/en-us/game/pvp/leaderboards/2v2' 
    html = get_html(url)
    links = get_name_links(html) # stage 2 end 
    for link in links:
        html_name = get_html(link)
        data = get_data(html_name)
        print(data)
        formated_data = data.split()
        
if __name__ == "__main__":
    main()