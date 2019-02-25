import requests
#Create Call and save answer Создание запроса и сохранение 
# его в переменную с вызовом на экран функции Принт
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

r = requests.get(url)
print('Ответ:', r.status_code)
#Обработка информации о каждой статье
submission_ids = r.json()
submission_dics = []

for submission_id in submission_ids[:30]:
    #создание отдельного ЭЙПИАЙ API для каждой статьи
    url = ('https://hacker-news.firebaseio.com/v0/'+str(submission_id)+'.json')
    submission_r = requests.get(url)
    print(url)
   