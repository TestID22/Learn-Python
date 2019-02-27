import webbrowser
import requests

url = ('http://grompe.org.ru/static/prog_comp_matrix_ru.html')
webbrowser.open(url)

r = requests.get(url)
print('Статус сервера', r.status_code)