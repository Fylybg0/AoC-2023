f = [[x for x in i] for i in open('input.txt', 'r').read().split('\n')]
starts = [((i, -1 if x == 1 else len(f)), (0, x*2-1)) for i in range(len(f[0])) for x in range(1, -1, -1)] + [((-1 if x == 1 else len(f[0]), i), (x*2-1, 0)) for i in range(len(f)) for x in range(1, -1, -1)]
dir = {(0, 1): {'"\\"': [(1, 0)], '"/"': [(-1, 0)], '"-"': [(-1, 0), (1, 0)], '"|"': [(0, 1)], '"."': [(0, 1)]},
       (1, 0): {'"\\"': [(0, 1)], '"/"': [(0, -1)], '"-"': [(1, 0)], '"|"': [(0, 1), (0, -1)],  '"."': [(1, 0)]}, 
       (0, -1): {'"\\"': [(-1, 0)], '"/"': [(1, 0)], '"-"': [(-1, 0), (1, 0)], '"|"': [(0, -1)],  '"."': [(0, -1)]}, 
       (-1, 0): {'"\\"': [(0, -1)], '"/"': [(0, 1)], '"-"': [(-1, 0)], '"|"': [(0, 1), (0, -1)],  '"."': [(-1, 0)]}}
mx = 0
print(starts)
for start in starts:
    visited = set()
    outcomes = [start]

    while outcomes != []:
        new = []
        for outcome in outcomes:
            q, p = outcome[0][0] + outcome[1][0], outcome[0][1] + outcome[1][1]
            if 0 <= q < len(f[0]) and 0 <= p < len(f) and ((q, p), outcome[1]) not in visited:
                visited.add(((q, p), outcome[1]))
                tile = '"' + f[p][q] + '"'
                for axe in dir[outcome[1]][tile]:
                    new.append(((q, p), axe))
        outcomes = new.copy()

    mx = max(len({i[0] for i in visited}), mx)


print(mx)