import re

phone = re.compile(r'\d\d\d-\d\d\d')
find_num = phone.search('dasdasd qweq wqweqwe asdddf a 423-977')
print(find_num.group())