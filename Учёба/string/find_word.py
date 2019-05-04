import os


f = open('testtext.txt', 'w')
f.write('hack hack buerak email')
f.close

word_list = ['h', 'hack']

f = open('testtext.txt', 'r')
read = f.readline()
formated_read = read.split()


words_num = 0
for word in word_list:
    for line in formated_read:
        if word == line:
            words_num += 1

print('Количество потворяющихся слов' , words_num)
