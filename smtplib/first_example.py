import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
'''в переменой smtpUbj хранится объект, т.е. всё верное мы создали
объект класса SMTP'''

print(type(smtpObj))