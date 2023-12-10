f = [[x for x in i] for i in open('input.txt', 'r').read().split('\n')]
dir = {'S': ((0, -1), (0, 1), (1, 0), (-1, 0)), '|': ((0, -1), (0, 1)), '-': ((-1, 0), (1, 0)), 'L': ((0, -1), (1, 0)), 'J': ((0, -1), (-1, 0)), '7': ((0, 1), (-1, 0)), 'F': ((0, 1), (1, 0))}

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

print(len(poses[0][1]))