import random


rand_list = ['One','two','three','four','five','six','seven']

def rand_item(random_list):
    rand_num = random.randint(0, len(random_list) -1)
    print(rand_num)

rand_item(rand_list)



