import math
from collections import Counter
from itertools import count

def is_prime(num):
    if num % 2 == 0:
        return False
    max = int(math.sqrt(num))+1
    for i in xrange(3,max,2):
        if num % i == 0:
            return False
    return True

def gen_primes():
    yield 2
    for i in count(3,2):
        if is_prime(i):
            yield i

def get_factors(num):
    max = num / 2 + 1
    if is_prime(num):
        return [num]
    factors = []
    for p in gen_primes():
        if p > max:
            break
        while num % p == 0:
            factors.append(p)
            num /= p

    return factors

def get_num_divisors(factors):
    result = 1
    for key, value in Counter(factors).items():
        result *= value +1
    return result

f_old = [3]
for i in count(3):
    f = get_factors(i+1)
    factors = sorted(f_old + f)[1:]
    divisors = get_num_divisors(factors)
    if divisors > 500:
        print i, i*(i+1)/2, factors, divisors
        break
    f_old = f
