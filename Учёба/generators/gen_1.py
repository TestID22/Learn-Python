example = [x ** 2 for x in range(1,5)]
print(example)


res = [x for x in range(1,10) if x % 2 == 0]
print(res)


new_res = [x + y for x in [0,1,2] for y in [100,200,300]]
print(new_res)



res_list = []
def func_1():
    for x in [0,1,2]:
        for y in [100,200,300]:
            res_list.append(x + y)
func_1()
print(res_list)