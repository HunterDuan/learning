'''class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return self.p*1.0 / self.q

print float(Rational(7, 2))
print float(Rational(1, 3))
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
    @property
    def grade(self):
        if self.score>=80:
            return 'A'
        elif self.score<60:
            return 'C'
        else:
            return 'B'
s = Student('Bob', 59)
print s.grade

s.score = 60
print s.grade

s.score = 99
print s.grade
class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
class Student(Person):
    __slots__ = ('score')
    def __init__(self,name,gender,score):
        super(Student,self).__init__(name,gender)
        self.score = score

s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print s.score'''
class Fib(object):
    def __call__(self,num):
        L=[0,1]
        for i in range(num-2):
            L.append(L[-1]+L[-2])
        return L

f = Fib()
print f(10)