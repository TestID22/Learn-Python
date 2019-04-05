#Используется для нахождения повторябщихся символов
#поиск букв в слове или предложении
vowels = ['a','b','h','g','s','o', '1']
word = 'Jon Snow and Khalisy 1'
found = []

for letter in word.lower():
    if letter in vowels:
        if letter not in found:
            found.append(letter)
found.sort()
print(found)