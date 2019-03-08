l = [lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4]

print(l[0](3))

for i in l:
    print(i(2))
    
#лямбда использует условные инструкции
lower = lambda x,y: x if x < y else y
print(lower(25,3))