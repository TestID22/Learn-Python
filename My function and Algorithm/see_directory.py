import os
#начало проекта
def day_walker(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir,name)
        print(path)

input()