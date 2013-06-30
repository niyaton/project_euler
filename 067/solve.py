import sys
from itertools import izip
lines = []
for line in open(sys.argv[1]):
    lines.append([ int(s) for s in line.split(' ') ])
print lines

while len(lines) != 1:
    l = lines.pop()
    maxs = [ max(l[i], l[i+1]) for i in xrange(len(l)-1) ]
    lines[-1] = [ i + j for i, j in izip(maxs, lines[-1]) ]
    print maxs
    print lines[-1]
