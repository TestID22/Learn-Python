import random

atack = 5
atack1 = random.randrange(1,10)
health = 20
damage = 3
trolls = 0
while health > 0:
    
    trolls += 1
    health -= damage
    print("Ваш Герой готов к послденей битве, он взмахнул мечом, и отсёк яйло Тролю нанеся ", atack)
    print('перед тем как отъехать в Валхалу, ты окучил ',trolls,'тролей')
print("Ваш Герой Пал")