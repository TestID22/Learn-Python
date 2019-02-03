pets = ['cat','dog','shars','cat','cat','bee','rabbit']
print(pets)
#удаляем повторяющиеся в списке элементы
while 'cat' in pets:
    pets.remove('cat')
print(pets)