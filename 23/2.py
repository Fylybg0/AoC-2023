f = [[x for x in i] for i in open('input.txt', 'r').read().strip().split('\n')]
axes = [(1, 0), (0, 1), (-1, 0), (0, -1)]
allowed = {'>': [(1, 0)], 'v': [(0, 1)], '<': [(-1, 0)], '.': [(1, 0), (0, 1), (-1, 0), (0, -1)], '#': []}
graph = {(x, i): [(x+axe[0], i+axe[1]) for axe in axes if 0 <= x+axe[0] < len(f[0]) and 0 <= i+axe[1] < len(f) and f[i+axe[1]][x+axe[0]] != '#'] for i in range(len(f)) for x in range(len(f[0]))}
start, end = (1, 0), (len(f[0]) - 2, len(f) - 1)
highest = 0

possible = {(start, (start, )): 0}

while possible != {}:
    new = {}
    for p in possible:
        for al in graph[p[0]]:
            if al == end:
                highest = max(highest, possible[p] + 1)
            elif al not in p[1]:
                if (al, p[1] + (al, )) in new:
                    new[(al, p[1] + (al, ))] = max(possible[p] + 1, new[al][0])
                else:
                    new[(al, p[1] + (al, ))] = possible[p] + 1
    possible = new
    print(len(possible))

print(highest)
