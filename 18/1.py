f = [(lambda x: [x[0], int(x[1]), x[2]])(i.split()) for i in open('input.txt', 'r').read().split('\n')]
dirs = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1)}
axes = [(1, 0), (0, 1), (-1, 0), (0, -1)]
pos = (0, 0)
blocks = [pos]

for i in f:
    blocks += [(pos[0] + dirs[i[0]][0] * x, pos[1] + dirs[i[0]][1] * x) for x in range(1, i[1] + 1)]
    pos = blocks[-1]

max_x, max_y, min_x, min_y = max(blocks, key=lambda x: x[0])[0] + 1, max(blocks, key=lambda x: x[1])[1] + 1, min(blocks, key=lambda x: x[0])[0] - 1, min(blocks, key=lambda x: x[1])[1] - 1

for i in range(min_y, max_y + 1):
    print(''.join(['#' if (x, i) in blocks else '.' for x in range(min_x, max_x + 1)]))

def findOutside(start):
    visited = [start]
    new = visited.copy()
    flag = True
    while flag:
        flag = False
        new_ = new.copy()
        new = []
        for i in new_:
            for axe in axes:
                q, p = i[0] + axe[0], i[1] + axe[1]
                if min_x <= q <= max_x and min_y <= p <= max_y and (q, p) not in visited and (q, p) not in new and (q, p) not in blocks:
                    new.append((q, p))
                    flag = True
        visited += new
        print(len(set(visited)))
    return len(set(visited))

output = (max_x - min_x + 1) * (max_y - min_y + 1) - findOutside((min_x, min_y))

print(output)