import csv

csvFile = open('base.csv', 'wt')
csvwriter = csv.writer(csvFile)
csvwriter.writerow(('Linkin', 'Park'))
for i in range(10):
    csvwriter.writerow((i, i+2))
csvFile.close