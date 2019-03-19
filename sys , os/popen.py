import os

my_dir = os.popen('dir /B').readlines()


new_my_dir = []
for line in my_dir:
    new_my_dir.append(line[:-1])
print(new_my_dir)
#используем генератор списков для удобочитаемости (слудуй кодексу Дзен Пайтон)
#или иди программируй на HTML
lines = [line[:-1] for line in my_dir]
print(lines)

