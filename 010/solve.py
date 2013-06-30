import math

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

print reduce(lambda a,b: a+b, get_primes())
