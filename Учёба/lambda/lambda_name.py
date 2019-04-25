#Учимся писать анонимные лямбда выражения(непоименнованые)

full_name = (lambda fname, sname: fname + ' ' + sname)
fname = input('')
sname = input('')

print(full_name(fname, sname))
#########################################################
#список из лямбда - выражений
lamdda_list = [lambda x: x + 1,
               lambda x: x * x,
               lambda x: x ** 2]

for i in lamdda_list:
    print(i(2))

print('Вызов первой Лямбды из списка',lamdda_list[0](1))