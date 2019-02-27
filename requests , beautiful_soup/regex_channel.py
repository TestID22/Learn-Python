import re 

#Символ канала "|" для регулярных выражений означает 'этот' или 'тот'
club = re.compile(r'Inter|Milan')
club_finder = club.search('''Самый лучший футбольный клуб который я знал это миланский Inter,
'а Milan уже потом''')
print(club_finder.group())