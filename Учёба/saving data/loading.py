import json

filename = 'numbers.json'
with open(filename)as r_obj:
    numbers = json.load(r_obj)
    print(numbers)