f = [i for i in open('input.txt', 'r').read().split('\n')]
col, row = [], []
for i in range(len(f)):
    if '#' not in f[i]:
        row.append(i)

for i in range(len(f[0])):
    if '#' not in [f[x][i] for x in range(len(f))]:
        col.append(i)

g = [(x, i) for i in range(len(f)) for x in range(len(f[0])) if f[i][x] == '#']

c = 0
for i in range(len(g)-1):
    for x in range(i+1, len(g)):
        v, h = abs(g[i][0] - g[x][0]), abs(g[i][1] - g[x][1])
        for r in col:
            if g[i][0] < r < g[x][0] or g[i][0] > r > g[x][0]:
                v += 999999
        for r in row:
            if g[i][1] < r < g[x][1] or g[i][1] > r > g[x][1]:
                h += 999999

        c += v + h

print(c)