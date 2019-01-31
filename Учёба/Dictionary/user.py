user = {'name':'Vitaliy',
        'first':'Alex',
        'second':'Lena'
}

for key,value in user.items():
    print('Key:', key)
    print('Value:', value)
    print(' ' *100)

#перебор словаря
favourite_languages = {'Alex':'C++',
                       'Sara':'Java',
                       'Lena':'C#',
                       'Pavel Cat':'Ruby',
                       'John Snow':'Python'
                       }
                    
friends = ['Alex','Lena']

for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print('Привет,',name.title(),'твой любимый язык программирования',favourite_languages[name])


