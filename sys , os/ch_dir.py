import os

path = ('d:\\')
os.listdir()
for name in os.listdir(path):
    pname = os.path.join(name)
    print(pname)