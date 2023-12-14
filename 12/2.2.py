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

def subCheck(com, idx, y, nums):
    o, r = 0, []
    for x in range(len(y)):
        if o >= len(com[:idx]):
            break
        if y[x] == '?':
            r.append(com[o])
            o += 1
        else:
            r.append(y[x])
    r = check(r)
    if r != []:
        return nums[:len(r)-1] == r[:-1]
    return nums[:len(r)] == r

#print(subCheck(['#', '.', '#', '#', '.', '.', '.', '.'], 5, ['?', '?', '.', '?', '.', '?', '?', '?', '?', '?'], [1,2,3]))

def checkk(x, y):
    return all([(x[i] in ['.', '?'] and  y[i] in ['.', '?']) or (x[i] in ['#', '?'] and y[i] in ['#', '?']) for i in range(len(x))])

def getLine(x, y):
    return [i for i in ''.join([('.' * (x[i]+1) if i != 0 else '.' * (x[i]) if (i == 0 and x[i] + 1 != 0) else '')  + '#' * y[i] for i in range(len(y))] + ['.' * (x[-1])])]


def findCombinations(comb, idx, pp, j, i):
    global cg
    if len(comb) == idx:
        #print(cg)
        b = [(1, 0)]
        new = []
        p = j.count('?')
        o, r = 0, []
        for x in range(len(i[0])):
            if o >= len(comb[:idx]):
                break
            if i[0][x] == '?':
                r.append(comb[o])
                o += 1
            else:
                r.append(i[0][x])
        
        s, o = [], 0
        for x in r:
            if x == '#':
                o += 1
            if x == '.' and o != 0:
                s.append(o)
                o = 0
        if o != 0:
            s.append(o)

        if i[1] == s:
            cg += 1
    else:
        if subCheck(comb[:idx], idx, i[0], i[1]):
            comb[idx] = '.'
            findCombinations(comb.copy(), idx + 1, pp, j, i)
            comb[idx] = '#'
            findCombinations(comb.copy(), idx + 1, pp, j, i)
#cg = 0
#findCombinations(['?', '?', '?', '?', '?'], 0, 5, ['?', '#', '?', '?', '#', '?', '?'], [['?', '#', '?', '?', '#', '?', '?'], [1, 2]])
#print(cg)

c = 0
k = 0
for i in f:
    k += 1
    print(k)
    a = [[]]
    for x in range(len(i[0])):
        if i[0][x] in ['#', '?']:
            a[-1].append(i[0][x])
        elif a[-1] != []:
            a.append([])
    if a[-1] == []:
        a = a[:-1]
    
    if len(a) == 1:
        print('brute')
        cg = 0
        jj = a[0].count('?')
        findCombinations(['.'] * jj, 0, jj, a[0], i)
        c += cg
    else:
        b = [(1, 0)]
        for j in a:
            new = []
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
            gr = { tuple(x): s.count(x) for x in s}

            for x in b:
                for z in gr:
                    if list(z) == i[1][x[1]:x[1] + len(z)]:
                        new.append((x[0] * gr[z], x[1] + len(z)))

            b = new.copy()

        
        c += sum([x[0] for x in b])
        print(c)
    #a = [item for item in itertools.product(*[['.', '#'] for _ in range(p)])]

    

print(c)
