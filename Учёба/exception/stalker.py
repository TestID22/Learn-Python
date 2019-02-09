filename = 'D:\Code\Python\Учёба\exception\Зона Поражения.txt'
#Считаем слова в книге
with open(filename)as read_stalker:
    reading = read_stalker.read()
    words = reading.split()
    num_words = len(words)
    print(num_words)