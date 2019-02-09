import json

filename = 'user.json'

with open(filename)as r_obj:
    text = r_obj.read()
    print('Ну привет',text)
input('Введите Enter')