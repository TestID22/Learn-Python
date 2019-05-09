#Задача состоит, в том чтобы выводить на экран повторяющиеся слова в потоке

previous = ' '
print("Введите 'exit' для выхода")
print("Введите 's' для вывода всех повторяющихся слов")
words = []
while True:
    word = input ()
    if word == 'exit': break
    if word == 's':
        print(words)
    elif word == previous:
        words.append(word)
        previos = word
        print ("Повторяющиеся слово " + word)
    previous = word
    
