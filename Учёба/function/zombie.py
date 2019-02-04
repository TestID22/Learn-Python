def getKilledZombie(alive_zombies,deadzombies):
    while alive_zombies:
        kilingZombie = alive_zombies.pop()
        print('Убиваем зомби:', kilingZombie.title())
        deadzombies.append(kilingZombie)

#параметр функции - список
def rip_zombies(killed_zombies):
        for kz in killed_zombies:
                print(kz.title(),'отправился на тот свет повторно')

game_zombies = ['tom','jessy','brandon']
zombies = []

getKilledZombie(game_zombies,zombies)
rip_zombies(zombies)
