#Генератор списков

l = [x + 1 for x in range(0,10)]
print(l)

#добавляем + 10 к списку l
l = [x + 10 for x in l]
print(l)
#Читаем фалй 1.txt со всеми символами внутри
f = open('1.txt')
lines = f.readlines()
print(lines)

#убираем в генераторе символ новых строк \n
lines = [line.rstrip() for line in lines]
print(lines)