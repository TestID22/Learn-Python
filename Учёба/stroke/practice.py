#1
for i in range(1,21):
    print(i)
#2
one_million = list(range(1,1000001))
print(one_million)
#3
print(min(one_million))
print(sum(one_million))
#4
not_even_number = list(range(1,20,2))
for i in not_even_number:
    print(i)
#5
third = list(range(3,30,3))
for i in third:
    print(i)
#6
square = []
for i in range(1,10):
    square.append(i**3)
print(square)

#7Добавляем в список square при помощи генератора кубы от 1 до 10
square = [value**3 for value in range(1,10)]
print(square)