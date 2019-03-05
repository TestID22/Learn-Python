def tester(start):
    state = start
    def nesterd(label):
        nonlocal state
        print(label, state)
        state += 1
    return nesterd

F = tester(1)
F('spam')
F('ham')