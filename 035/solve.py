import math
def is_prime(num):
    lim = int(math.sqrt(num)) + 2
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in xrange(6, lim, 6):
        if num % (i-1) == 0 or num % (i+1) == 0:
            return False
    return True

def gen_primes():
    yield 2
    yield 3
    for i in xrange(6,1000000,6):
    #for i in xrange(6,100,6):
        if is_prime(i-1):
            yield i-1
        if is_prime(i+1):
            yield i+1

def gen_rotations(s):
    tmp = s
    for i in range(len(s)-1):
        tmp = tmp[-1] + tmp[:-1]
        yield tmp


for i in gen_primes():
    #print i, list(gen_rotations(str(i)))
    #print i, map(is_prime, [int(s) for s in gen_rotations(str(i))])
    if False not in map(is_prime, [int(s) for s in gen_rotations(str(i))]):
        print i

