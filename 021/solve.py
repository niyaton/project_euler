def gen_divisors(n):
    for i in xrange(1,n/2+1):
        if n % i == 0:
            yield i

def d(n):
    return sum(gen_divisors(n))


def gen_amicables():
    for i in range(10001):
        tmp = d(i)
        if tmp != i and d(tmp) == i:
            print i, d(i)
            yield i
print sum(gen_amicables())
    
