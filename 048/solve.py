import math
from itertools import repeat
def gen_powers():
    for i in range(1,1001):
        yield reduce(lambda a,b: a*b, repeat(i,i))
        #yield math.pow(i, i)

print str(sum(gen_powers()))[-10:]
