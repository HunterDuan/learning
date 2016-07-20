'''import time

def performance(unit):
    def per_decorator(f):
        def fn(*args,**kw):
		    t3=time.time()
		    g=f(*args,**kw)
		    t4=time.time()
		    print 'call %s() in %fs'% (f.__name__,(t4-t3))
		    print 'call %s() in %fs %s' % (f.__name__, (t4-t3)*1000,unit)
            return g
        return fn
	return per_decorator
@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))
print factorial(10)'''
import time, functools

def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            return f(*args,**kw)
        return wrapper
    return perf_decorator
@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial.__name__