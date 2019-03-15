class Super():
    def __init__(self, x):
        self.x = x

class Sub(Super):
    def __init__(self, x, y):
        Super.__init__(self, x)
        '''адаптированный код'''
        
x = Sub(1, 2)