import shelve

fielnames = ('name','age','pay','job')
maxfield = max(len(f) for f in fielnames)
db = shelve.open('class-shelve')

while True:
    key = input('\n Введите ключик=>')

    if not key:
        break
    
    try:
        record = db[key]
    except:
        print('Такого ключа нет %s' % key)
    else:
        for field in fielnames:
            print(field.ljust(maxfield),'=>',getattr(record, field))
