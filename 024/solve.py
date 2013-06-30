def gen_permutations(max_num):
    p = 1
    for i in range(1,max_num+1):
        p *= i
        yield p

def gen_sequence(index, max_digit):
    seq_candidates = range(max_digit+1)

    permutations = list(gen_permutations(max_digit))
    permutations.reverse()

    sum = 0
    for i in range(max_digit):
        c = (index - sum - 1) / permutations[i]
        sum += c * permutations[i]
        yield seq_candidates.pop(c)
    yield seq_candidates[0]

seq = list(gen_sequence(1000000, 9))
print ''.join([str(i) for i in seq])
