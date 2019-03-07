def find_min_func(*args):
    res = args[0]
    for i in args[1:]:
        if i < res:
            res = i
            return res

print(find_min_func(1, 91, 5, 2, 20, -1, 23, 13))
