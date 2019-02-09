import json



userinfo = input('Введите имя и я запомню его:')
filename = 'user.json'
with open(filename, 'w')as f_obj:
    json.dump(userinfo, f_obj)
    print('Хорошо' ,userinfo, 'я тебя запомнила')
