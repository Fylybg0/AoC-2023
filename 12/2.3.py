import itertools

f = [(lambda x: [([j for j in x[0]] + ['?']) * 4 + [j for j in x[0]], [int(j) for j in x[1].split(',')] * 5])(i.split()) for i in open('input.txt', 'r').read().split('\n')]

def subCheck(x, y):
    #print(x)
    #print(y)
    #print('/////////')
    #print(all([(x[i] in ['.', '?'] and  y[i] in ['.', '?']) or (x[i] in ['#', '?'] and y[i] in ['#', '?']) for i in range(len(x))]))
    
    return all([(x[i] in ['.', '?'] and  y[i] in ['.', '?']) or (x[i] in ['#', '?'] and y[i] in ['#', '?']) for i in range(len(x))])

def check(x, y):
    return all([(x[i] in ['.', '?'] and  y[i] in ['.', '?']) or (x[i] in ['#', '?'] and y[i] in ['#', '?']) for i in range(len(x))])

def getLine(x, y):
    return [i for i in ''.join([('.' * (x[i]+1) if i != 0 else '.' * (x[i]) if (i == 0 and x[i] + 1 != 0) else '')  + '#' * y[i] for i in range(len(y))] + ['.' * (x[-1])])]

def findCombinations(comb, idx, nones, left, y, con):
    a = 0
    if len(comb) == idx + 1:
        comb = comb[:-1] + (left, )
        #print(comb)
        if check(getLine(comb, con), y):
            print(comb)
            c = 1
            for x in comb:
                for z in range(1, x + 1):
                    c *= z
            return c
        return 0
    for i in range(left + 1):
        comb = comb[:idx] + (i, ) + comb[idx + 1:]
        #print(comb, idx)
        line = getLine(comb, con)
        #print(line)
        if subCheck(y[:idx], line):
            a += findCombinations(comb, idx + 1, nones, left - i, y, con)
    return a

#???? ? ???? ? ???? ? ???? ? ???? 2, 2, 2, 2, 2


c = 0
for i in f:
    lenght = sum(i[1]) + len(i[1])
    nones = (len(i[0]) - sum(i[1]) - len(i[1]) + 1)
    positions = i[1].copy() + [None] * nones

    print(findCombinations((0,) * (len(i[1]) + 1), 0, nones, nones, i[0], i[1]))

    

print(c)
