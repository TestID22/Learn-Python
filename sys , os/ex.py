import sys 
#разбираемся с аргументами командной строки 
'''
скрипт принимает аргумент командной строки,
который всегда принмает значение [1], [0] - значение 
принимает путь и  название самого файла
'''
d = r'code' if len(sys.argv) == 1 else sys.argv[1]
print(d)
input()
print(sys.argv[0])