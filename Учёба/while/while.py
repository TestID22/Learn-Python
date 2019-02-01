prompt = 'Молви друг и выйди '
message = ''
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    elif message == 'exit':
        active = False

    else:
        print(message)