import shelve

db = shelve.open('class-shelve')
for key in db:
    print(db[key].name, db[key].pay)

elliot = db['elliot']

print(elliot.lastName())