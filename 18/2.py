f = [(lambda x: [int(x[-2]), int(x[2:-2], 16)])(i.split()[2]) for i in open('input.txt', 'r').read().split('\n')]
#f = [(lambda x: [{'R': 0, 'D': 1, 'L': 2, 'U': 3}[x[0]], int(x[1]), x[2]])(i.split()) for i in open('input.txt', 'r').read().split('\n')]
dirs = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
axes = [(1, 0), (0, 1), (-1, 0), (0, -1)]
pos = (0, 0)
y_blocks = {}
x_ranges = {}
y_ranges = {}
x_blocks = {}
data = {}
c = 0
print(f)
for idx, i in enumerate(f):
    print(idx)
    if i[0] in [1, 3]:
        for x in range(i[1] + 1):
            new_y = pos[1] + (x * dirs[i[0]][1])
            if new_y in y_blocks:
                y_blocks[new_y] += (pos[0], )
            else:
                y_blocks.update({new_y: (pos[0], )})

        new_range = tuple(sorted((pos[1], pos[1] + (i[1] * dirs[i[0]][1]))))
        if pos[0] in y_ranges:
            y_ranges[pos[0]] += (new_range, )
        else:
            y_ranges[pos[0]] = (new_range, )
        pos = (pos[0], pos[1] + (i[1] * dirs[i[0]][1]))
    else:
        for x in range(i[1] + 1):
            new_x = pos[0] + (x * dirs[i[0]][0])
            if new_x in x_blocks:
                x_blocks[new_x] += (pos[1], )
            else:
                x_blocks.update({new_x: (pos[1], )})

        new_range = tuple(sorted((pos[0], pos[0] + (i[1] * dirs[i[0]][0]))))
        if pos[1] in x_ranges:
            x_ranges[pos[1]] += (new_range, )
        else:
            x_ranges[pos[1]] = (new_range, )
        pos = (pos[0] + (i[1] * dirs[i[0]][0]), pos[1])
    c += i[1]

for pos_y in y_blocks:
    a = 2
    sub_c = 0
    y_blocks[pos_y] = tuple(sorted(y_blocks[pos_y]))
    if (y_blocks[pos_y], ) + (x_ranges.get(pos_y, tuple()), ) in data:
        c += data[(y_blocks[pos_y], ) + (x_ranges.get(pos_y, tuple()), )]
    else:
        for i in range(len(y_blocks[pos_y]) - 1):
            if (y_blocks[pos_y][i], y_blocks[pos_y][i+1]) not in x_ranges.get(pos_y, []):
                if y_blocks[pos_y][i+1] != y_blocks[pos_y][i] + 1:
                    x_blocks[y_blocks[pos_y][i] + 1] = tuple(sorted(x_blocks[y_blocks[pos_y][i] + 1]))
                    for x in range(0, len(x_blocks[y_blocks[pos_y][i] + 1]), 2):
                        if x_blocks[y_blocks[pos_y][i] + 1][x] <= pos_y <= x_blocks[y_blocks[pos_y][i] + 1][x+1]:
                            sub_c += y_blocks[pos_y][i+1] - y_blocks[pos_y][i] - 1
                            break
        data[(y_blocks[pos_y], ) + (x_ranges.get(pos_y, tuple()), )] = sub_c
        c += sub_c

print(c)

#952408144115
#67622758357096