from itertools import count, izip
def gen_seq():
    for i in count():
        for c in str(i):
            yield c

target = [1, 10, 100, 1000, 10000, 100000, 1000000]
p = 1
for i, c in izip(count(), gen_seq()):
    if i in target:
        p *= int(c)
        target.pop(0)
    if not target:
        break
print p
