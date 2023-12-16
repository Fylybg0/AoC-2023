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
    rr = check(r)
    if rr != [] and r[-1] != '.':
        return nums[:len(rr)-1] == rr[:-1]
    return nums[:len(rr)] == rr

def subCheck2(com, idx, y, routes):
    o, r = 0, []
    for x in range(len(y)):
        if o >= len(com[:idx]):
            break
        if y[x] == '?':
            r.append(com[o])
            o += 1
        else:
            r.append(y[x])
    rr = check(r)
    for route in routes:
        if rr != [] and r[-1] == '.':
            if route[:len(rr)-1] == rr[:-1]:
                return True
        else:
            return True
    return False

#print(subCheck(['#', '.', '#', '#', '.', '.', '.', '.'], 5, ['?', '?', '.', '?', '.', '?', '?', '?', '?', '?'], [1,2,3]))

def checkk(x, y):
    return all([(x[i] in ['.', '?'] and  y[i] in ['.', '?']) or (x[i] in ['#', '?'] and y[i] in ['#', '?']) for i in range(len(x))])

def getLine(x, y):
    return [i for i in ''.join([('.' * (x[i]+1) if i != 0 else '.' * (x[i]) if (i == 0 and x[i] + 1 != 0) else '')  + '#' * y[i] for i in range(len(y))] + ['.' * (x[-1])])]


def findCombinations(comb, idx, pp, line, route):
    global cg
    if pp == idx:
        #print(comb)
        #print(cg)
        o, r = 0, []
        for x in range(len(line)):
            if o >= len(comb[:idx]):
                break
            if i[0][x] == '?':
                r.append(comb[o])
                o += 1
            else:
                r.append(line[x])
        
        s, o = [], 0
        for x in r:
            if x == '#':
                o += 1
            if x == '.' and o != 0:
                s.append(o)
                o = 0
        if o != 0:
            s.append(o)

        if route == s:
            cg += 1
            if cg % 1000 == 0:
                print(cg)
    else:
        if subCheck(comb[:idx+1], idx+1, line, route):
            findCombinations(comb.copy(), idx + 1, pp, line, route)
        comb[idx] = '#'
        if subCheck(comb[:idx+1], idx+1, line, route):
            findCombinations(comb.copy(), idx + 1, pp, line, route)

def findCombinationsMore(comb, idx, jCount, line, routes):
    global d
    if jCount == idx:
        d.append(comb)
        if len(d) % 100000 == 0:
            print(len(d))
    else:
        if subCheck2(comb[:idx], idx, i, routes):
            comb[idx] = '.'
            findCombinationsMore(comb.copy(), idx + 1, jCount, line, routes)
            comb[idx] = '#'
            findCombinationsMore(comb.copy(), idx + 1, jCount, line, routes)

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
        findCombinations(['.'] * jj, 0, jj, a[0], i[1])
        print(cg)
        c += cg
    else:
        b = [(1, 0)]
        for j in a:
            new = []
            p = j.count('?')
            d, possible_following = [], [i[1][possible[1]:] for possible in b]
            findCombinationsMore(['.'] * p, 0, p, i[0], possible_following)
            s = []
            for z in d:
                o, r = 0, []
                for x in range(len(j)):
                    if j[x] == '?':
                        r.append(z[o])
                        o += 1
                    else:
                        r.append(j[x])
                s.append(tuple(check(r)))
                
            gr = {}
            for x in s:
                if x in gr:
                    gr[x]  += 1
                else:
                    gr[x] = 1

            for x in b:
                for z in gr:
                    if list(z) == i[1][x[1]:x[1] + len(z)]:
                        new.append((x[0] * gr[z], x[1] + len(z)))

            b = new.copy()

        
        c += sum([x[0] for x in b])
        print(c)

print(c)
