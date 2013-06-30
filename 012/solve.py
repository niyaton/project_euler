import sys
from itertools import count
from itertools import izip

def get_factors(num):
    for i in range(2, num/2 + 1):
        if num % i == 0:
            yield i

def get_num_factors(num):
    result = 2
    for i in range(2, num/2 + 1):
        if num % i == 0:
            result += 1
    return result

def gen_triangle(n):
    sum = n*(n+1)/2
    yield sum
    for i in count(sum+1):
        sum += i
        yield sum

input = sys.argv[1]
for i, triangle in izip(count(), gen_triangle(int(input))):
    num_factors = get_num_factors(triangle)
    print i , triangle, num_factors
    if i > 10:
        break
