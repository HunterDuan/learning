def factorial(n):
    result=n
	for i in range(1,n):
	    result*=i
	return result
def power(x,n):
    result=1
	for i in range(n):
	    result*=x
	return result