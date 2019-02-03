def getKilledZombie(alive_zombies,deadzombies):
    for kilingZombie in alive_zombies:
        kilingZombie = alive_zombies.pop()
        deadzombies.append(kilingZombie)

alive_zombies = ['tom','kotl','jack','chuck']
deadzombies = []
getKilledZombie(alive_zombies,deadzombies)
print(deadzombies)
