class Person(object):
    def __init__(self, name, gender, **kw):
        self.name=name
        self.gender=gender
        for i,j in kw.iteritems():
            setattr(self,i,j)

p = Person('Bob', 'Male', age=18, course='Python')
print p.age
print p.course