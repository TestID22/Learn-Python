import os
#os.walk возвращает dirpath dirnames filenames
for (dirname, subshere, filehere) in os.walk('.'):
    print('['+ dirname +']')
    for fname in filehere:
        print(os.path.join(dirname, fname))