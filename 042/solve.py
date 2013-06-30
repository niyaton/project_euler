from string import ascii_uppercase
from itertools import count
import csv

print ascii_uppercase
uppercase = ['_']
uppercase.extend(ascii_uppercase[::])


def gen_triangles():
    for i in count(1):
        yield i * (i+1) / 2 

word_values = []
for row in csv.reader(open('words.txt')):
    for w in row:
        word_values.append(sum(map(uppercase.index, w)))
print max(word_values)

lim = max(word_values)
triangles = []
for t in gen_triangles():
    if t > lim:
        break
    triangles.append(t)

print map(lambda v: v in triangles, word_values).count(True)
