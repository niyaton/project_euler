import csv
from itertools import count,izip
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
reader = csv.reader(open('names.txt'))
def get_scores():
    for row in reader:
        for i, s in izip(count(1), sorted(row)):
            val = sum([a.index(c)+1 for c in s])
            yield i*val 
        break
print sum(get_scores())
