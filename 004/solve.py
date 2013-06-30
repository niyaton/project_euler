def palindromic():
    for i in range(999*999,1,-1):
        s = str(i)
        l = len(s) / 2
        left = s[0:l]
        right = s[-l:]
        if left == right[::-1]:
            yield i

for i in palindromic():
    for j in range(999, 99, -1):
        if i % j == 0 and i / j <= 999:
            print i, j, i/j
            exit(0)
