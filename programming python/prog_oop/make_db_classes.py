import shelve 
from person_start import Person
from manager import Manager

elliot = Person('Elliot Anderson', 33, 40000)
darling = Person('Darling', 35, 1000)
tyrell = Manager('Tyrell', 36, 100000)

db = shelve.open('class-shelve')
db['elliot'] = elliot
db['darling'] = darling
db['tyrell'] = tyrell

db.close()