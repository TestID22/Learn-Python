import webbrowser
import requests

url = 'https://www.google.com'
webbrowser.open(url)

r = requests.get(url)

print('Статус сервера', r.status_code)