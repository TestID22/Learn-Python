'''
скрипт ищет самый большой файл с кодо Py
в единственном каталоге.
Поиск выполняется в каталоге библиотеки 
если в аргументе командной строки не был указан другой
катаолог.
'''

import os, glob, sys

dirname = r'd:\python 3.6\lib' if len(sys.argv) == 1 else sys.argv[1]
allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])