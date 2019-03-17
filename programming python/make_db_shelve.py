from initdata import elliot, darling
import shelve

db = shelve.open('people-shelve')
db['elliot'] = elliot
db['darling'] = darling

print(db['darling'])
db.close()
