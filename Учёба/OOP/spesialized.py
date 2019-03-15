class Super():
    def method(self):
        print('In Super.method')
    def delegate(self):
        self.action

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print('In Replacer.method')

class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):
    def action(self):
        print('In Provider.action')

if __name__ == "__main__":
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method
        print('\n Provider')
        x = Provider()
        x.delegate()