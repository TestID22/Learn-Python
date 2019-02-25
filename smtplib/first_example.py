# -*- coding: utf-8 -*-
import smtplib

#Работа с электронной почтой
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

'''в переменой smtpUbj хранится объект, т.е. всё верное мы создали
объект класса SMTP'''
print(type(smtpObj))

#Будь вежлив, скажи Привет!
print(smtpObj.ehlo())
#Включаем систему шифрования почтового сервера
print(smtpObj.starttls())
"""smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted
Если появляется, Ошибка, доступа небезопасных приложений, требуется
открыть доступ на почтовом сервере
"""

print(smtpObj.login('YOUR_EMAIL@gmail.com',
                    'Your_PASS'))

TEXT = input('ВВеди Текс Сообщение(только Латинские): ')

smtpObj.sendmail('YOUR_EMAI@gmail.com',
                 'TARGET_EMAIL@yahoo.com',
                 'Subject: Test \n' + TEXT)
        
smtpObj.quit()