f = [sorted([[int(z) for z in x.split(',')] for x in i.split('~')]) for i in open('input.txt', 'r').read().split('\n')]
holding = {i: set() for i in range(len(f))}
blocks = [{i} for i in range(len(f))]

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
    for block in blocks:
        fell2 = True
        new_blocks = set()
        while fell2:
            fell2 = False
            if f[min(block, key=lambda x: f[x][0][2])][0][2] != 1:
                for b in block:
                    f[b][0][2], f[b][1][2] = f[b][0][2] - 1, f[b][1][2] - 1
                flag = False
                for idi, block2 in enumerate(f):
                    for b in block:
                        if overlap(f[b], block2) and b != idi:
                            holding[b].add(idi)
                            new_blocks.add(idi)
                            flag = True
                if flag:
                    for b in blocks:
                        f[b][0][2], f[b][1][2] = f[b][0][2] + 1, f[b][1][2] + 1
                    block.update(new_blocks)
                else:
                    fell, fell2 = True, True
                    holding[b] = set()

reverse_holdings = {i: set() for i in range(len(f))}
for i in holding:
    for x in holding[i]:
        reverse_holdings[x].add(i)

m = set()
for i in holding:
    if len(holding[i]) >= 2:
        m.update(holding[i])

for i in holding:
    print(i, holding[i])

n = {i for x in holding for i in holding[x]}
m.update({i for i in range(len(f)) if i not in n})

print(m)
print(len(m))

#902 too high
#748 too high
#697 too high
#687