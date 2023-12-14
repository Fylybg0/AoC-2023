import itertools

f = [(lambda x: [[j for j in x[0]], [int(j) for j in x[1].split(',')]])(i.split()) for i in open('input.txt', 'r').read().split('\n')]

def check(x):
    a = []
    p = 0
    for i in x:
        if i == '#':
            p += 1
        if p != 0 and i != '#':
            a.append(p)
            p = 0
    if p != 0:
        a.append(p)
    return a

c = 0
for i in f:
    p = i[0].count('?')
    a = [item for item in itertools.product(*[['.', '#'] for _ in range(p)])]
    
    for z in a:
        o, b = 0, []
        for x in range(len(i[0])):
            if i[0][x] == '?':
                b.append(z[o])
                o += 1
            else:
                b.append(i[0][x])
        c += 1 if i[1] == check(b) else 0

print(c)
