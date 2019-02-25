import requests
#Создание ссылки в переменной и сохранение ответа и статуса за
url = ('https://api.github.com/search/repositories?q=language:python&sort=stars')
r = requests.get (url)
print('Статус ответа', r.status_code)
respose = r.json()
print(respose.keys())

name, stars = [], []

print('\n Всего репозиториев по метке ПАЙТОН',respose['total_count'])
#Анализ информации о репозиториях
repositorie_dict = respose['items']
#Проверяем длинну 
print('Репозиториев ', len(repositorie_dict))
#Анализ информаци по первому репозиторию
repo_dict = repositorie_dict[0]
print('Ключи:', len(repo_dict))
for key in sorted(repo_dict):
    print(key)
print('Получаем информацию по ключам')
print('name ', repo_dict['name'])
print('Owner ', repo_dict['owner']['login'])
print('Description',repo_dict['description'])
    



input()

