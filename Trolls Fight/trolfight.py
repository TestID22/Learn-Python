import random

atack = 5
health = 20
damage = 3
trolls = 0

print("Ваш Герой готов к послденей битве")
while health > 0:
    atack1 = random.randrange(1,10)
    trolls += 1
    health -= damage
    print("Герой  взмахнул мечом, и отравил Тролю на тот свет, нанеся ", atack1)
    print('перед тем как отъехать в Валхалу, ты окучил ',trolls,'тролей')
print("Ваш Герой Пал")