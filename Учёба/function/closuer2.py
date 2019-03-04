def maker(n):
    def action(x):
        return x * n
    return action

f = maker(2)
print(f(4))
print(f(8))