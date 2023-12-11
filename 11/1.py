f = [i for i in open('input.txt', 'r').read().split('\n')]

z = 0
for i in range(len(f)):
    if '#' not in f[-1-i-z]:
        f.insert(-i-1-z, '.'*len(f[0]))
        z += 1
z = 0
for i in range(len(f[0])):
    if '#' not in [f[x][i+z] for x in range(len(f))]:
        for x in range(len(f)):
            f[x] = f[x][0:i+z] + '.' + f[x][i+z:]
        z += 1

g = [(x, i) for i in range(len(f)) for x in range(len(f[0])) if f[i][x] == '#']

c = 0
for i in range(len(g)-1):
    for x in range(i+1, len(g)):
        c += abs(g[i][0] - g[x][0]) + abs(g[i][1] - g[x][1])

print(c)