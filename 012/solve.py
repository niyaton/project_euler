import math
from itertools import izip, count, product

def is_prime_num(num):
    max = int(math.sqrt(num))
    for i in xrange(3, max+1, 2):
        if num % i == 0:
            return False
    return True

def get_primes():
    yield 2
    for i in xrange(3, 2000000, 2):
        if is_prime_num(i):
            yield i


primes = []
for i, p in izip(count(1), get_primes()):
    primes.append(p)
    if i == 5:
        break

print primes
print len(primes)
for i in product(primes, repeat=5):
    p = reduce(lambda a,b:a*b, i)
    print p
