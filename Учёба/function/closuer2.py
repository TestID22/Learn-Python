x = 88
def f1():
    x = 100
    def f2():
        print(x)
    f2()
f1()
print(x)