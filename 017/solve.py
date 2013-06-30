base1 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
'nine']
base1019 = []
base1019.extend(['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen'])
base1019.extend(['sixteen', 'seventeen', 'eighteen', 'nineteen'])

base10 = ['', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
'eighty', 'ninety']
base100 = ['hundred']

base100 = ['']
for o in base1:
    if o == '':
        continue
    base100.append(o + ' hundred')

def gen_words():
    for h in base100:
        for t in base10:
            for o in base1:
                if h == '' or ( t == '' and o == ''):
                    yield '%s %s %s' % (h, t, o)
                else:
                    yield '%s and %s %s' % (h, t, o)
        for t in base1019:
            if h == '':
                yield '%s %s' % (h, t)
            else:
                yield '%s and %s' % (h, t)
    yield 'one thousand'

for s in gen_words():
    print s

print sum( [ len(s.replace(' ','')) for s in gen_words() ])
