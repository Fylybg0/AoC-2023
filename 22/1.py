f = sorted([sorted([[int(z) for z in x.split(',')] for x in i.split('~')]) for i in open('input.txt', 'r').read().strip().split('\n')], key = lambda x: x[0][2])
#f = sorted([sorted([[int(z) for z in x.split(',')] for x in i.split('~')]) for i in open('input.txt', 'r').read().split('\n')])

holding = {i: set() for i in range(len(f))}

def rangeOverlap(x, y):
    return y[0] <= x[0] <= y[1] or y[0] <= x[1] <= y[1] or x[0] <= y[0] <= x[1] or x[0] <= y[1] <= x[1]

def overlap(x, y):
    return rangeOverlap((x[0][0], x[1][0]), (y[0][0], y[1][0])) and rangeOverlap((x[0][1], x[1][1]), (y[0][1], y[1][1])) and rangeOverlap((x[0][2], x[1][2]), (y[0][2], y[1][2]))
k = 0
fell = True
while fell:
    print(k)
    k += 1
    fell = False
    for idx, block in enumerate(f):
        print(idx)
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

m = set()
for i in holding:
    if len(holding[i]) >= 2:
        m.update(holding[i])

print()
print(f)
a = [[[1, 0, 1], [1, 2, 1]], [[0, 0, 2], [2, 0, 2]], [[0, 2, 2], [2, 2, 2]], [[0, 0, 3], [0, 2, 3]], [[2, 0, 3], [2, 2, 3]], [[0, 1, 4], [2, 1, 4]], [[1, 1, 5], [1, 1, 6]]]

for i in f:
    if i not in a:
        print('false')
        break
else:
    print(True)

for i in holding:
    print(i, holding[i])

n = {i for x in holding for i in holding[x]}
l = {x for i in holding for x in holding[i] if len(holding[i]) == 1}
print(m)
m.update({i for i in range(len(f)) if i not in n})
m = {i for i in m if i not in l}

print(m)
print(len(m))

#902 too high
#748 too high
#697 too high