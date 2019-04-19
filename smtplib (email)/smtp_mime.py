import smtplib
from email.mime.text import MIMEText

msg = MIMEText('This is a Text for you')

msg['Subject'] = 'Тут Тема Письма'
msg['From'] = 'vitaliiseptember@gmail.com'
msg['To'] = 'vitaliiseptember@gmail.com'

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo() #приветсвие
s.starttls() #шифрование
s.login('vitaliiseptember@gmail.com','mypass')
s.send_message(msg)
s.quit
