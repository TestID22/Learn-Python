#Перебор по символу For
file = open('text.txt')
for i in file.readlines():
    print(i)

#Перебор по символу из файла while
file = open('text.txt')
while True:
    f = file.read(1)
    if not f:
        break
    print(f)