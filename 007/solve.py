import math
from itertools import count
from itertools import izip

#for i in count(2):
#    if i / math.log(i) > 100002:
#        print i

def is_prime_num(num):
    max = int(math.sqrt(num))
    for i in range(2, max+1):
        if num % i == 0:
            return False
    return True

prime = (i for i in count(2) if is_prime_num(i))
for i, prime in izip(count(1), prime):
    if i == 10001:
        print i, prime
        exit(0)
