'''result=[]
for x in range(3):
    for y in range(3):
	    result.append((x,y))
print result'''

'''girls=['alice','bernice','clarice']
boys=['chirl','arnold','bob']
print [b+'+'+g for b in boys for g in girls if b[0]==g[0]]'''
girls =['alice','bernice','clarice']
boys=['chirl','arnold','bob']
letterGirls={}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]	