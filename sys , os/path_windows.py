import sys
import os

print(sys.platform)
if sys.platform[:1] == 'w':
    print('Привет Окна')
 
#возвращает пути к модулям пайтона
path_all = sys.path
print('path_all', sys.path)
#возвращает текущую директорию
g = os.getcwd()
print(g)

