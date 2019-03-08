l = list(range(-5,6))

print(filter((lambda x: x > 0), range(-5,6)))
####цикл for божественный
res = []
for x in range(-5,6):
    if x > 0:
        res.append(x)
        print(res)
