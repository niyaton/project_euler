import math
def get_largest_factor(num):
    max = int(math.sqrt(num))
    for i in range(max, 1, -1):
        if num % i == 0:
            return i

def get_factors(num):
    max = int(math.sqrt(num))
    for i in range(max, 1, -1):
        if num % i == 0:
            yield i

print list(get_factors(13195))
for i in get_factors(600851475143):
    if len(list(get_factors(i))) == 0:
        print i
        exit(0)
