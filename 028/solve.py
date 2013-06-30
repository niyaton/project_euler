max = 1001
def gen_diagonals():
    for i in xrange(3, max+1, 2):
        edge = i * i
        yield edge
        for j in range(3):
            edge -=i - 1
            yield edge
        
for i in gen_diagonals():
    print i

print sum(gen_diagonals()) + 1
