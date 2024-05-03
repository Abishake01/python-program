'''
from obj import vollyball
class make():
    a=5
    pass
pr=make()
print(pr.a)
b=make(vollyball)
print(b.name)
'''

class person():
    def __init__(self,name,age):
        self.names=name#self.name=name is declare we use different var also but use similar name only
        self.age=age
name=input('Enter a name: ')
age=int(input('Enter a Age: '))
a=person(name,age)
print(a.names)
print(a.age)
