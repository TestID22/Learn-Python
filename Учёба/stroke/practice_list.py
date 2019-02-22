#перебираем список задом на перёд
odd = list(range(1,300, 1))
print(odd[::-1])
#end = в одну строку
for i in odd[::-1]:
    print(i, end='')