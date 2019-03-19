import os

os.chdir('d:\\code\\python\\учёба\\practice')
#полуаем директорию
print('direction' ,os.getcwd())
#use shell

print('direct', os.system('dir'))


text = os.popen('type for.py').read()
print(text)
listening = os.popen('type primer.py').readlines()
print(listening)
input('Enter')
os.system('type for.py')