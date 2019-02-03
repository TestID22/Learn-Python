#пишем функцию с параметрами animal_type и animal_name
def animal(animal_name, animal_type = 'dog'):
    #выводит инфу о животине
    print('\n I have a', animal_type)
    print('\n My ', animal_type ,' name is ', animal_name)

animal('Хамстер')
