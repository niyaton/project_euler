def fibonacci(limit):
    yield 1
    old = 1
    current = 2
    while current < limit:
        yield current
        new = old + current
        old = current
        current = new

print sum([i for i in fibonacci(4000000) if i % 2 == 0])
