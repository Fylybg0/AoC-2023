f = [[x for x in i] for i in open('input.txt', 'r').read().strip().split('\n')]
axes = [(1, 0), (0, 1), (-1, 0), (0, -1)]
allowed = {'>': [(1, 0)], 'v': [(0, 1)], '<': [(-1, 0)], '.': [(1, 0), (0, 1), (-1, 0), (0, -1)], '#': []}
graph = {(x, i): [(x+axe[0], i+axe[1]) for axe in axes if 0 <= x+axe[0] < len(f[0]) and 0 <= i+axe[1] < len(f) and f[i+axe[1]][x+axe[0]] != '#'] for i in range(len(f)) for x in range(len(f[0])) if f[i][x] != '#'}
start, end = (1, 0), (len(f[0]) - 2, len(f) - 1)
highest = 0
possible = {(start, (start, )): 0}
new_graph = {}
new_lenghts = {}

print(len([0 for i in graph if len(graph[i]) > 2]))

def findCrossroads(pos, visited):
    if len(graph[pos]) > 2 or pos == start or pos == end:
        return visited + [pos]
    for i in graph[pos]:
        if i not in visited:
            return findCrossroads(i, visited + [pos])

for i in range(len(f)):
    for x in range(len(f[0])):
        if f[i][x] != '#' and len(graph[(x, i)]) > 2 or (x, i) == start or (x, i) == end:
            new_graph[(x, i)] = []
            for j in graph[(x, i)]:
                l = findCrossroads(j, [(x, i)])
                if l is not None:
                    new_graph[(x, i)].append(l[-1])
                    new_lenghts[((x, i), l[-1])] = len(l) - 1

print(len(new_graph))

while possible != {}:
    new = {}
    print(len(possible))
    for p in possible:
        for al in new_graph[p[0]]:
            if al == end:
                print(p[1])
                highest = max(highest, possible[p] + new_lenghts[(p[0], al)])
            elif al not in p[1]:
                new[(al, p[1] + (al, ))] = possible[p] + new_lenghts[(p[0], al)]
    possible = new

print(highest)
