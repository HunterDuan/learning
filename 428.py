'''class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student:%s,%s,%s)'%(self.name,self.gender,self.score)
	__repr__ = __str__
s = Student('Bob', 'male', 88)
print s
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if self.score>s.score:
            return -1
        if self.score<s.score:
            return 1
        return cmp(self.name,s.name)

L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)
class Fib(object):
    def __init__(self, num):
        L=[0,1]
        for i in range(num-2):
            L.append(L[-1]+L[-2])
        self.num=L
	def __str__(self): 
	    return str(self.num)
    def __len__(self): 
	    return len(self.num) 
f = Fib(10)
print f
print len(f)'''
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)
    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)
    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.q)

    def __str__(self):
	    c = gcs(self.p, self.q)
        return '%s/%s'%(self.p/c, self.q/c)

    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2