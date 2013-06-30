from operator import itemgetter
import math
from itertools import count
def is_prime(num):
    lim = int(math.sqrt(num)) + 2
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in xrange(6, lim, 6):
        if num % (i-1) == 0 or num % (i+1) == 0:
            return False
    return True

def calc_quadratic(n,a,b):
    return n*n + a*n + b

def gen_primes_from_quadratic(a,b):
    for i in count():
        p = calc_quadratic(i,a,b)
        if is_prime(abs(p)):
            yield p
        else:
            return

m = (0, 0, 0)
for a in xrange(-999,1000):
    for b in xrange(-999,1000):
        v = (len(list(gen_primes_from_quadratic(a,b))), a, b)
        m = max(m, v, key=itemgetter(0))
            
print m, m[1] * m[2]
