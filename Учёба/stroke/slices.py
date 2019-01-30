#Перебор срезов и работа со срезами work with slices
players = ['icardi','naingolan','politano','candreva']
print(players[0:2])
print('\n')
print('Inter держится на игроках:')
for player in players[0:3]:
    print('\t',player.title())