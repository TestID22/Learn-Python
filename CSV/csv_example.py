import csv

csvFile = open('base.csv', 'a')
writer = csv.writer(csvFile)
writer.writerow(('Номер', 'Имя' , 'Класс'))
for line in range(2):
    writer.writerow(('12','Ваня','Нуб'))
csvFile.close