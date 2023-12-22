f = [i for i in open('input.txt', 'r').read().split('\n')]
start = [[(x, i) for x in range(len(f[0])) if f[i][x] == 'S'] for i in range(len(f)) if 'S' in f[i]][0][0]
len_f = len([0 for i in range(len(f)) for x in range(len(f[0])) if f[i][x] != '#'])
possible = {(0, 0): {start}}
axes = [(1, 0), (0, 1), (-1, 0), (0, -1)]
p = {(x, y): {((x + axe[0] + len(f[0])) % len(f[0]), (y + axe[1] + len(f)) % len(f)): (-1 if x + axe[0] < 0 else 1 if x + axe[0] >= len(f[0]) else 0, -1 if y + axe[1] < 0 else 1 if y + axe[1] >= len(f) else 0) for axe in axes if f[(y + axe[1] + len(f)) % len(f)][(x + axe[0] + len(f[0])) % len(f[0])] != '#'} for y in range(len(f)) for x in range(len(f[0]))}
counter = 0
data = {}
print(p[start])
blocked = []

for i in range(5000):
    print(i, len(possible), len(blocked))
    new = {}
    for dim in possible:
        if len(possible[dim]) in [39, 41]:
            counter += len(possible[dim])
            blocked.append(dim)
        else:
            for pos in possible[dim]:
                for n in p[pos]:
                    new_dim = (dim[0] + p[pos][n][0], dim[1] + p[pos][n][1])
                    if new_dim in new:
                        new[new_dim].add(n)
                    elif new_dim not in blocked:
                        new[new_dim] = {n}
    possible = new

print(possible)
print(sum(len(possible[i]) for i in possible) + counter, counter)