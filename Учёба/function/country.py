def get_dead_zombies(alive_zombies,dead_zombies):
    all_zobies = alive_zombies, ' ', dead_zombies
    return all_zobies

while True:
    killed_zombies = input('Сколько ходячих ты убил?')
    print('Ты убил ', killed_zombies ,' ходяков')
    if killed_zombies == 'quit':
        break

    see = 20

    answer = get_dead_zombies(killed_zombies, see)
    print(answer)