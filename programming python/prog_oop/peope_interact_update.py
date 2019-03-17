from person_start import Person
import shelve

fieldnames = ('name','age','pay','job')
db = shelve.open('class-shelve')

while True:
    key = input('\nВведите ключ: ')
    if not key:
        break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?',age='?',pay='?')
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\t\tnew?=>' %(field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record
db.close()