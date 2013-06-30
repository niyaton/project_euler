from itertools import count
l = []
c = count(1)
for i in range(5):
    l.append(c.next())

for i in c:
    #print l,
    p = reduce(lambda a,b: a*b, l)
    if len(str(p)) > 1000:
        break
    ans = (p,l)
    l.pop(0)
    l.append(i)
print ans
