'''
скрипт находит наибольший файл с кодом Py
в дереве каталогов используя os.walk рекурсивный обход
'''
import os, sys, pprint

trace = False
if sys.platform.startswith('win'):
    dirname = r'd:\code\python' #windows
else:
    dirname = '/usr/lib/python' #*nix

allsize = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace: print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsize.append((fullsize, fullname))
    
allsize.sort()
print(allsize[:2])
print(allsize[-2:])