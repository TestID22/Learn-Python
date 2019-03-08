def action(x):
    return x + 10

ex_list = list(range(1,22))
act = list(map(action, ex_list))
print(act)

#луковица прям
lister = list(map((lambda x: x + 3),ex_list[::1]))
print(lister)