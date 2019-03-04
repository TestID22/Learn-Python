def multilication(a,b):
    return a * b

print(multilication(5,2))

def multilication_5(b):
    return 5 * b
print(multilication_5(3))


def mul(a):
    def helper(b):
        return a * b
    return helper

print(mul(2)(5))   