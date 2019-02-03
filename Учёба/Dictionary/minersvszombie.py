#Создаём пустой список, для хранения Зомборей
zombies = []
#Создаём армию зомби для игры Терриконщики против ЗОМБИ
for zombie_number in range(0,30):
    new_zombie = {'speed':'slow','color':'green','points':5}
    zombies.append(new_zombie)

#Выкатываем первых 3 зомби используя срез и меняем им характеристики 
for zombie in zombies[:3]:
    if zombie['color'] == 'green':
        zombie['color'] ='red'
        zombie['points'] = 10
        zombie['speed'] = 'fast'
print(zombies[:5])
print('Всего созданно', len(zombies))