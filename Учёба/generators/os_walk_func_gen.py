import os

dir_b = []
for (a, b, c) in os.walk('e:\фото'):
    dir_b.append(c)

print(dir_b)