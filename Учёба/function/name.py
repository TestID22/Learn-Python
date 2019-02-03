def formated_name(first_name,last_name,second_name=''):
        full_name = first_name + ' ' + second_name + ' ' + last_name
        if second_name:
            full_name = first_name + ' ' + second_name + ' ' + last_name
        return full_name

name = formated_name('Alex','Shepard','lee')
print(name)
        
#Возвращамем аргументы функцией return
def build_person(first_name, last_name, age = ''):
    full_name = {'first':first_name,'last':last_name}
    if age:
        full_name['age'] = age
    return full_name
 
name_1 = build_person('Paul','Walker', age = 25)
print(name_1)