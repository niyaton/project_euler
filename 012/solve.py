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

def gen_triangle():
    sum = 0
    for i in count(1):
        sum += i
        yield sum

print list(get_factors(500))
#for i, triangle in izip(count(), gen_triangle()):
#    num_factors = get_num_factors(triangle)
#    if num_factors > 500:
#        print i , triangle, num_factors
#        break
