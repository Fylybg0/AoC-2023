import itertools

f = [(lambda x: [([j for j in x[0]] + ['?']) * 4 + [j for j in x[0]], [int(j) for j in x[1].split(',')] * 5])(i.split()) for i in open('input.txt', 'r').read().split('\n')]

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
k = 0
for i in f:
    k += 1
    a = [[]]
    for x in range(len(i[0])):
        if i[0][x] in ['#', '?']:
            a[-1].append(i[0][x])
        elif a[-1] != []:
            a.append([])
    if a[-1] == []:
        a = a[:-1]
        
    b = [(1, 0)]
    for j in a:
        new = {}
        p = j.count('?')
        d = [item for item in itertools.product(*[['.', '#'] for _ in range(p)])]
        s = []
        for z in d:
            o, r = 0, []
            for x in range(len(j)):
                if j[x] == '?':
                    r.append(z[o])
                    o += 1
                else:
                    r.append(j[x])
            s.append(check(r))
        
        for z in s:
            for x in b:
                print(x)
                if z == i[1][x[1]:x[1] + len(z)] or z == []:
                    if x[1] + len(z) in new:
                        new[x[1] + len(z)][0] += 1
                    else:
                        new[x[1] + len(z)] = [1, x[0]]
        b = [(new[z][0]*new[z][1], z) for z in new]

    
    c += b[0][0]
    print(b[0][0])
    
    #a = [item for item in itertools.product(*[['.', '#'] for _ in range(p)])]

    

print(c)
