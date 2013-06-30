def total1000():
    for i in range(1000):
        for j in range(1000):
            if i > j:
                continue
            k = 1000 - i - j
            if k > 0 or j > k:
                yield (i,j,k)
            
triple = list(total1000())
ans = [(i,j,k) for i,j,k in triple if i*i + j*j == k*k]
for i in ans:
    print reduce(lambda a,b:a*b, i)
