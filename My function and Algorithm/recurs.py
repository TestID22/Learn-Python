#пример простой рекурсии
def hello(x):
    x += 1
    print('Смотри как я считаю', x)
    return hello(x)

hello(1)