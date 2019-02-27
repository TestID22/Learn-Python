import re 

#Поиск эмейлов 
email_regex = re.compile('[A-Za-z0-9\._+]+@[A-Za-z]+\.(com)')
file = [x.rstrip() for x in open('email_list.txt')]
print(file)
file = str(file)
e_finder = email_regex.search(str(file))
print(e_finder.group())