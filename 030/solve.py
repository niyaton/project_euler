from itertools import combinations
from itertools import product
from math import pow
digits = range(10)

for i in range(10):
    p = pow(9,5)*i
    print i, p, len(str(int(p)))

def gen_answers():
    for r in range(8):
        for c in product(digits, repeat=r):
            s = int(sum( [ pow(i,5) for i in c ] ))
            c_str = ''.join([str(i) for i in c])
            s_str = str(s)
            if s_str == c_str:
                print s
                yield s
print sum(gen_answers())
