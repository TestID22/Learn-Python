l1 = 'abc'
l2 = 'zxy'
#zip объединяет элементы 
zip_res = (list(zip(l1,l2)))
print(zip_res)



d = {'a': 1, 'b': 2}
l = iter(d)
print(next(l))


for i in d:
    print(i, d[i])