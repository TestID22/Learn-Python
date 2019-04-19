import csv

csvFile = open('base.csv', 'a')
writer = csv.writer(csvFile)
writer.writerow(('Номер', 'Имя' , 'Класс'))
csvFile.close