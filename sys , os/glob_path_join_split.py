import glob
import os

dirname = 'D:\\code\\Python\\sys, os'
print(dirname)

for file in glob.glob(dirname + '/*'):
    a, b = os.path.split(file)
#os.listdir() - берёт текущий каталог 
for file in os.listdir('.'):
    print(' =>',os.path.join(dirname, file))

input()