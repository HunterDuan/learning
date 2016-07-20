'''class Person(object):
    pass
p1 = Person()
p1.name = 'Bart'
p2 = Person()
p2.name = 'Adam'
p3 = Person()
p3.name = 'Lisa'
L1 = [p1, p2, p3]
L2 = sorted(L1,key=lambda x:(x.name))
print L2[0].name
print L2[1].name'''
class Person(object):
    def __init__(self, name, score):
        self.name=name
        self.__score=score
p = Person('Bob', 59)
try:
    print p.__score
except AttributeError:
    print ('attributeError')
print p.name
print p.__score