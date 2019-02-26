import requests
#к локалке проверяем опрос запрос...тесты, с Джанго
r = requests.get('http://localhost:8000')
print(r)