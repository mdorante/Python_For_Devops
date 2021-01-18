'''
simple class example
'''


class MyClass():
    def some_method(self):
        print(f'Say hi to {self}')


myObject = MyClass()
myObject.some_method()


class MyOtherClass():
    def __init__(self, name):
        self.name = name


myOtherObject = MyOtherClass('Dude')
print(myOtherObject.name)
