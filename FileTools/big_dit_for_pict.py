'''
dev - Vitaliy September
'''
import sys, glob, os


dirname = input('Введите имя дир: ') 

allfile = []

get_allfile = glob.glob(dirname + os.sep +'*.jpg')#glob.glob - ищет все файлы по заданным параметрам
#циклом проходимся по директории, берём размеры, и названия, и добавляем ОДНИМ КОРТЕЖЕМ 
#get_size and picture = 
for picture in get_allfile:
    get_size = os.path.getsize(picture)
    allfile.append((get_size, picture))

allfile.sort()

print('Батюшки, а самая большая картинка это: ', allfile[-1:])
print('Самая "лёгкая" картинка:', allfile[:1])
input('ВВедите любую кнопку для')