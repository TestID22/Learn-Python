#Используется для нахождения повторябщихся символов
#поиск букв в слове или предложении
vowels = ['a','b','h','g','s','o',]
word = 'Jon Snow'
found = []

for letter in word.lower():
    if letter in vowels:
        if letter not in found:
            found.append(letter)

print(found)