def new_func(x):
    for i in x:
        yield i * 2

list_ex = list(range(1,10))
g = new_func(list_ex)
print(next(g))
print(next(g))
print(next(g))
print(next(g))