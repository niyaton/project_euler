import math
#print '9'*1000
#print 1.0E999
#max = int('9'*1000)
#print max

#print 1000 / 5

i = int('1' + '0'*200)
print i*i*i*i*i
print len(str(i*i*i*i*i))

#print i*(i-1)*(i-2)*(i-3)*(i-4)
#print len(str((i*(i-1)*(i-2)*(i-3)*(i-4))))
#print len(str(((i+1)*(i-1)*(i-2)*(i-3)*(i-4))))

s = i - 2
l = []
for i in range(5):
    l.append(s+i)
#print reduce(lambda a,b: a*b, l)

from itertools import count
for i in count():
    p = reduce(lambda a,b: a*b, l)
    if len(str(p)) > 1000:
        break
    print p
    print len(str(p))
    l.pop(0)
    l.append(l[-1]+1)
    print l
    

