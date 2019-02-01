prompt = '\nВведите в каких городах вы бывали '
prompt += '\nКогда закончишь баловаться ,введи уже наконец "quit" +'

city = ''
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print('Я был в таких городах : ',city.title(), '!.')