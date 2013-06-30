def squares(limit):
    for i in range(1,limit+1):
        yield i * i

def square(limit):
    s = sum(range(1, limit+1))
    return s * s

print sum(squares(100)) - square(100)


