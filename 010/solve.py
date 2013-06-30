import math
from itertools import count

def is_prime_num(num):
    max = int(math.sqrt(num))
    if num == 2:
        return True
    for i in xrange(3, max+1, 2):
        if num % i == 0:
            return False
    return True

def get_primes():
    yield 2
    for i in count(3,2):
        if i > 2000000:
            break
        if is_prime_num(i):
            yield i

print reduce(lambda a,b: a+b, get_primes())
