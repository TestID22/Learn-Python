for i in range(1,5):
    print("\t", i)
print('\n')
#помещаем в переменную строку по функции list
numbers = list(range(1,56))
print(numbers)
print('\n')
#чётные числа
even_numbers = list(range(2,102,2))
print(even_numbers)
print('\n')
#циклом фор вычисляем квадраты от 1 до 10 и записываем их в список squares
squares = []
for value in range(1,11):  
    squares.append(value**2)
print(squares)

