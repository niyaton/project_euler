l = list()
for i in range(1,20+1):
    for j in l:
        if i % j == 0:
            i = i / j
    l.append(i)
print l
print reduce(lambda a,b: a*b, l)
