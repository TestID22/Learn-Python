import shelve

db = shelve.open('peple-shelve')
for key in db:
    print('\n key =>',db[key])
    print(db['elliot'])
db.close()