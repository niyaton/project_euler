import math

def is_prime_num(num):
    for i in xrange(6, int(math.sqrt(num))+2, 6):
        if num % (i-1) == 0:
            return False
        elif num % (i+1) == 0:
            return False
    return True

def get_primes():
    yield 2
    yield 3
    for i in xrange(6,2000000,6):
        if is_prime_num(i-1):
            yield i - 1
        if is_prime_num(i+1):
            yield i + 1

print sum(get_primes())
