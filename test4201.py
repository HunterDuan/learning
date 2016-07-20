'''import math

def add(x,y,f):
    return f(x)+f(y)	
print add(25,9,math.sqrt)
def calc_prod(lst):
    def lazy_prod():
        def prod(x,y):
            return x*y
        return reduce(prod,range(1,len(lst)+1)) 
    return lazy_prod
f = calc_prod([1, 2, 3, 4])
print f()
def count():
	fs = []
	for i in range(1, 4):
		def f(i):
			def g():
				return i * i
			return g
		fs.append(f(i))
	return fs
f1, f2, f3 = count()
print f1(), f2(), f3()
import time
def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print 'call %s() in %fs' % (f.__name__, (t2 - t1))
        return r
    return fn
@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)'''
import time
def performance(unit):
    def per_decorator(f):
        def fn(*args,**kw):
		    t3=time.time()
		    g=f(*args,**kw)
			t4 = time.time()
			t = (t4 - t3) * 1000 if unit=='ms' else (t4 - t3)
			print 'call %s() in %f %s' % (f.__name__, t, unit)
            return g
        return fn
	return per_decorator
@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))
print factorial(10)#给出调用函数的时间ms

