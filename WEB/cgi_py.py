#!D:\Python 3.6
import cgi

form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title> Тут обработчик </title>')
if not 'user' in form:
    print('<h1> Кто ты чучело?</h1>')
else:
    print('<h2>Привеи %s</h2>' % cgi.escape(form['user'].value))