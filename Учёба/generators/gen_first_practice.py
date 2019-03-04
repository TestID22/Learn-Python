#Генератор списков

l = [x + 1 for x in range(0,10)]
print(l)

#добавляем + 10 к списку l
l = [x + 10 for x in l]
print(l)

#Читаем фалй 1.txt со всеми символами внутри
#убираем в генераторе символ новых строк \n
print('код из 3х строк')
f = open('1.txt')
lines = f.readlines()
lines = [line.rstrip() for line in lines]
print(lines)

#Сокращаем код  убирает символ окончания строки
print('Короткий список = код в одной строке')
short_code_lines = [line.rstrip() for line in open('1.txt')]
print(short_code_lines)