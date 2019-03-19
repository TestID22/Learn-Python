def func_min(*args):
    res = args[0]
    for i in args[1:]:
        if i < res:
            res = i
    return res
            

print(func_min(3,17,3,9,19))