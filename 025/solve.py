from itertools import count,izip
def gen_fibonacci():
    f1 = 1
    f2 = 1
    yield f1
    yield f2
    while True:
        f3 = f2 + f1
        yield f3
        f1 = f2
        f2 = f3

for i, f in izip(count(1), gen_fibonacci()):
    if len(str(f)) >= 1000:
        print i, f
        break
