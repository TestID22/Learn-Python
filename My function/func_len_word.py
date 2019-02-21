#Функция которая проверяет длинну слова(основа для создания функции, парсинга телефонных номеров,
# эмейлов)
def find_len(word):
    for i in word:
        if len(i) == 3:
            print(i)
            print('Слово из трёх букв')

words_list = ['Her','want','take','me','a','job']
find_len(words_list)