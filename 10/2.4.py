f = [[x for x in i] for i in open('input.txt', 'r').read().split('\n')]
dir = {'S': ((0, -1), (0, 1), (1, 0), (-1, 0)), '|': ((0, -1), (0, 1)), '-': ((-1, 0), (1, 0)), 'L': ((0, -1), (1, 0)), 'J': ((0, -1), (-1, 0)), '7': ((0, 1), (-1, 0)), 'F': ((0, 1), (1, 0))}
get_out = {(0, 1): ['|J7.', '|LF.'], (0, -1): ['|J7.', '|LF.'], (-1, 0): ['-JL.', '-7F.'], (1, 0): ['-JL.', '-7F.']}
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
z = [['.' if (x, i) not in poses else f[i][x] for x in range(len(f[i]))] for i in range(len(f))]

for i in range(len(f)):
    for x in range(len(f[0])):
        if f[i][x] == 'S':
            z[i][x] = '|'


def way_to_get_out(x):
    did, a, unc = True, [(i[0] + 0.5, i[1] + 0.5) for i in x], False
    visited = a.copy()
    print(a)
    while did and not unc:
        new, did = [], False
        for pos in a:
            for axe in axes:
                p, q = pos[0] + (axe[0] / 2), pos[1] + (axe[1] / 2)
                print((p, q))
                if 0 <= p < len(z[0]) and 0 <= q < len(z):
                    print(p, q)
                    if (pos[0] + axe[0], pos[1] + axe[1]) not in visited:
                        print([p, q])
                        try:
                            if axe[0] == 0:
                                if z[int(q)][int(p-0.5)] in get_out[axe][0] and z[int(q)][int(p+0.5)] in get_out[axe][1]:
                                    new.append((pos[0] + axe[0], pos[1] + axe[1]))
                                    visited.append((pos[0] + axe[0], pos[1] + axe[1]))
                                    did = True
                            else:
                                if z[int(q-0.5)][int(p)] in get_out[axe][0] and z[int(q+0.5)][int(p)] in get_out[axe][1]:
                                    new.append((pos[0] + axe[0], pos[1] + axe[1]))
                                    visited.append((pos[0] + axe[0], pos[1] + axe[1]))
                                    did = True
                        except: 
                            unc = True
                else:
                    unc = True
        a = new.copy()
    print(a, visited)
    return unc

closed_tiles = []
for i in range(len(z)):
    for x in range(len(z[0])):
        if (x, i) not in poses and (x, i) == (127, 87) and not way_to_get_out([(x, i)]):
            closed_tiles.append((x, i))
print(len(closed_tiles))
print(closed_tiles)
'''
for i in range(len(f)):
    print(''.join([z[i][x] if (x, i) in poses else 'X' if (x, i) in closed_tiles else 'O' for x in range(len(f[i]))]))
'''
'''
for i in z:
    print(*i, sep='')'''