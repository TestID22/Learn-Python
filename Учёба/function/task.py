#Task для перебора имён в списке
def make_magicians_great(namelist,namelist_2):
    while namelist:
        name = namelist.pop()
        print('Great ' +  name)
        namelist_2.append(name)

def show_magicians(users):
    for user in users:
        print(user)

magicians = ['David Blane','David','Davids']
great = []

make_magicians_great(magicians[:],great)
show_magicians(great)
print(magicians)