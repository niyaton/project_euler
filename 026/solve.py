from collections import defaultdict

def divide(num):
    p = 1
    seq = []
    mods = set()
    counter = defaultdict(int)
    while p != 0:
        #print mods
        #print counter
        if p < num:
            seq.append(0)
            #print '[*10]'
            p *= 10
        else:
            #print '[%d/%d]' % (p,num)
            d = p / num
            p = p % num
            #print mods, p
            #if p in mods:
            #    break
            if counter[p] == 2:
                break
            seq.append(d)
            mods.add(p)
            counter[p] += 1
            p *= 10
    return (seq, p != 0)

def count_repeat(seq):
    tail = seq[-1]
    while seq:
        l = len(seq)
        if l % 2 == 0:
            if seq[:l/2] == seq[l/2:]:
                return seq[:l/2],l
            
        seq.pop(0)
    return [tail], 1


#print divide(6)
m = 1
for i in xrange(1,1000):
    print i, 1.0 / i
    seq, flag = divide(i)
    if flag:
        (seq, l) = count_repeat(seq)
        print i, seq, count_repeat(seq)
        if l > m:
            m = l
            ml = i
print ml

