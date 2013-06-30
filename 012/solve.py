import math
from itertools import permutations, izip
import sys

primes = [2, 3, 5, 7, 9, 11, 13, 17, 23, 29, 31, 37, 41, 43, 47, 53, 59]

def is_triangle(num):
    n = (math.sqrt(8*num + 1) - 1)/2
    if n == int(n):
        print int(n)
    return n == int(n)

#while True:
#    line = sys.stdin.readline().strip()
#    print is_triangle(int(line))
ans = set()
#for i in permutations(primes, 5):
#    product = 1
#    for p, exp in izip(i, l):
#        product *= math.pow(p,exp)
#    if is_triangle(product):
#        print i, product, is_triangle(product)
#        ans.add(product)

def search(l):
    for i in permutations(primes, len(l)):
        product = 1
        for p, exp in izip(i, l):
            product *= math.pow(p,exp)
        if is_triangle(product):
            print i, product, is_triangle(product)
            ans.add(product)

#l = [1, 1, 4, 4, 4]
#l = [3, 4, 4, 4]
#search(l)

l = [1, 1, 1, 2, 2, 6]
search(l)
l = [3, 1, 2, 2, 6]
search(l)
l = [3, 5, 2, 6]
search(l)



#l = [1, 10, 22]
#search(l)

print min(ans)
