from itertools import count, izip
from collections import Counter
def gen_divs():
    yield 2
    yield 3
    for i in count(6,6):
        yield i - 1
        yield i + 1

def gen_factors(num):
    org = num
    for p in gen_divs():
        if p > org * org:
            break
        if num % p == 0:
            while num % p == 0:
                yield p
                num /= p
    if num > 1:
        yield num

bases = []
max_a = 100
numbers = range(2,max_a+1)
specials = []
for a in range(2, max_a+1):
    factors = Counter((gen_factors(a)))
    if a not in numbers:
        continue
    p = a
    if p * a <= max_a:
        specials.append([])
    else:
        continue
    while p <= max_a:
        specials[-1].append(p)
        numbers.remove(p)
        p *= a
    print a
        
print numbers
print specials

b = 100
s = 0
for i in specials:
    products = set()
    for index, n in izip(count(1), i):
        for r, j in izip(xrange(b-1), count(2 * index,index)):
            products.add(j)
    s += len(products)
print s + len(numbers) * (b-1)
