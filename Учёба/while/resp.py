#Cоздаём словарь в который поместим имена и ответы
responses = {}

#флаг 
active = True
while active:
    #Cпрашиваем имя
    name = input('Введите ваше имя:')
    response = input('Ваш ответ:')
    responses[name] = response
    

#проверка флага

    repeat = input('Хотите ввести новые данные в словарь yes/no')
    if repeat == 'no':
        active = False
for name, response in responses.items():  
    print('\n Опрос завершён')  
    print(name, 'Ты крутой Хацкер твой ответ',response)