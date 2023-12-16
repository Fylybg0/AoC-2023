f = [[x for x in i] for i in open('input.txt', 'r').read().split('\n')]
dir = {(0, 1): {'"\\"': [(1, 0)], '"/"': [(-1, 0)], '"-"': [(-1, 0), (1, 0)], '"|"': [(0, 1)], '"."': [(0, 1)]}, 
       (1, 0): {'"\\"': [(0, 1)], '"/"': [(0, -1)], '"-"': [(1, 0)], '"|"': [(0, 1), (0, -1)],  '"."': [(1, 0)]}, 
       (0, -1): {'"\\"': [(-1, 0)], '"/"': [(1, 0)], '"-"': [(-1, 0), (1, 0)], '"|"': [(0, -1)],  '"."': [(0, -1)]}, 
       (-1, 0): {'"\\"': [(0, -1)], '"/"': [(0, 1)], '"-"': [(-1, 0)], '"|"': [(0, 1), (0, -1)],  '"."': [(-1, 0)]}}
pos = (-1, 0)
visited = set()
outcomes = [(pos, (1, 0))]

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

out = {i[0] for i in visited}
for i in range(len(f)):
    print(''.join(['#' if (x, i) in out else '.' for x in range(len(f[0]))]))


print(len(out))