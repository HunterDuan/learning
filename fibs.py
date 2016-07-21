'''def fibs(num):
    result=[0,1]
    for i in range(num-2):
	    result.append(result[-2]+result[-1])
    return result 
print fibs(10)'''

def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}
def store(data,full_name):
    names=full_name.split()
    if len(names)==2: names.insert(1,'')
    labels='first','middle','last'
    for label,name in zip(labels,names):
        people=lookup(data,label,name)
    if people:
	    people.append(full_name)
    else:
	    data[label][name]=[full_name]
def lookup(data,label,name):
    return data[label].get(name)
Mynames={}
init(Mynames)
store(Mynames,'Magnus lie Het')
store(Mynames,'Robin Hegi')
store(Mynames,'Robin Hdge')
print lookup(Mynames,'first','Robin')