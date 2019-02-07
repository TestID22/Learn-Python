#Создание файлов Ворда и запись в них данных
with open('1.doc','w') as word_file:
    word_file.write('Пробуем в ворд записать разную информацию\n')
    word_file.write('И тут Разное')

with open('1.doc','r') as word_file:
    reading = word_file.read()
    print(reading)
