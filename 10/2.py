f = [[x for x in i] for i in open('input.txt', 'r').read().split('\n')]
dir = {'S': ((0, -1), (0, 1), (1, 0), (-1, 0)), '|': ((0, -1), (0, 1)), '-': ((-1, 0), (1, 0)), 'L': ((0, -1), (1, 0)), 'J': ((0, -1), (-1, 0)), '7': ((0, 1), (-1, 0)), 'F': ((0, 1), (1, 0))}
axes = [(0, -1), (0, 1), (1, 0), (-1, 0)]


for i in range(len(f)):
    for x in range(len(f[0])):
        if f[i][x] == 'S':
            start = (x, i)


poses = [(start, [])]
a = 0
while not (len(poses) == 2 and poses[0][0] == poses[1][0]):
    new = []
    for pos in poses:
        for axe in dir[f[pos[0][1]][pos[0][0]]]:
            p, q = pos[0][0] + axe[0], pos[0][1] + axe[1]
            if 0 <= p < len(f[0]) and 0 <= q < len(f) and (p, q) not in pos[1] and f[q][p] != '.':
                if (axe[0] * -1, axe[1] * -1) in dir[f[q][p]]:
                    new.append(((p, q), pos[1] + [(pos[0][0], pos[0][1])]))
    poses = new.copy()
    a += 1

poses = poses[0][1] + poses[1][1] + [poses[0][0]]
unclosed_tiles = []
closed_tiles = []


for i in range(len(f)):
    for x in range(len(f[0])):
        if (x, i) not in poses and (x, i) not in unclosed_tiles + closed_tiles:
            a, unc, clo, did = [(x, i)], False, False, True
            while did:
                did = False
                for pos in a:
                    for axe in axes:
                        p, q = pos[0] + axe[0], pos[1] + axe[1]
                        if 0 <= p < len(f[0]) and 0 <= q < len(f):
                            if (p, q) not in poses and (p, q) not in a and (p, q) not in unclosed_tiles + closed_tiles:
                                a.append((p, q))
                                did = False
                        else:
                            unc = True
            print(unc)
            if unc:
                unclosed_tiles += a.copy()
            else:
                closed_tiles += a.copy()

print((14, 3) in poses)
print(unclosed_tiles)
print(closed_tiles)
print(len(set(closed_tiles)))

for i in range(len(f)):
    print(''.join(['O' if (x, i) in unclosed_tiles else 'X' if (x, i) in closed_tiles else f[i][x] for x in range(len(f[i]))]))
