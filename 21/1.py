f = [i for i in open('input.txt', 'r').read().split('\n')]

start = [[(x, i) for x in range(len(f[0])) if f[i][x] == 'S'] for i in range(len(f)) if 'S' in f[i]][0][0]
possible = [start]
axes = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(64):
    new = []
    for p in possible:
        for axe in axes:
            x, y = p[0] + axe[0], p[1] + axe[1]
            if 0 <= x < len(f[0]) and 0 <= y < len(f) and f[y][x] != '#' and (x, y) not in new:
                new.append((x, y))
    possible = new.copy()

print(len(possible))