#вложенные лямбда -вырвжек
def action(x):
    return lambda y: x + y

act = action(2)
act(3)
print(act(3))