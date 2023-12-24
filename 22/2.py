f = sorted([sorted([[int(z) for z in x.split(',')] for x in i.split('~')]) for i in open('input.txt', 'r').read().strip().split('\n')], key = lambda x: x[0][2])

holding = {i: set() for i in range(len(f))}

def rangeOverlap(x, y):
    return y[0] <= x[0] <= y[1] or y[0] <= x[1] <= y[1] or x[0] <= y[0] <= x[1] or x[0] <= y[1] <= x[1]

def overlap(x, y):
    return rangeOverlap((x[0][0], x[1][0]), (y[0][0], y[1][0])) and rangeOverlap((x[0][1], x[1][1]), (y[0][1], y[1][1])) and rangeOverlap((x[0][2], x[1][2]), (y[0][2], y[1][2]))

fell = True
while fell:
    fell = False
    for idx, block in enumerate(f):
        '''if idx % 100 == 0:
            print(idx)'''
        fell2 = True
        while fell2:
            fell2 = False
            if block[0][2] != 1:
                block[0][2], block[1][2] = block[0][2] - 1, block[1][2] - 1
                flag = False
                for idi, block2 in enumerate(f):
                    if overlap(block, block2) and idx != idi:
                        holding[idx].add(idi)
                        flag = True
                if flag:
                    block[0][2], block[1][2] = block[0][2] + 1, block[1][2] + 1
                else:
                    fell, fell2 = True, True
                    holding[idx] = set()

reverse_holdings = {i: set() for i in range(len(f))}
for i in holding:
    for x in holding[i]:
        reverse_holdings[x].add(i)

def getFallen(start):
    p, save = {start}, set()
    visited = set()
    flag = True
    while flag and p != save:
        new, flag, save = set(), False, p
        for block in p:
            for up in reverse_holdings[block]:
                if all(i in p for i in holding[up]):
                    new.add(up)
                    flag = True
                else:
                    new.add(block)
        visited.update(new)
        p = new
    return len([i for i in visited if i != start])

c = 0
for i in range(len(f)):
    c += getFallen(i)

print(c)
