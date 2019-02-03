def get_albums(artist,albums,year = ' '):
    name = {'first':'artist','second':'albums'}
    full_inf = artist + ' ' + albums
    return full_inf

while 1:
    artist_name = input('Введите группу: ')
    if artist_name == 'quit':
        break

    albums_name = input('введите альбом: ')
    if albums_name == 'quit':
        break
    
    name = get_albums(artist_name,albums_name)
    print(name)

