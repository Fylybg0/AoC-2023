f = [i for i in open('input.txt', 'r').read().split('\n')]
w, h = len(f[0]), len(f)
start = [[(x, i) for x in range(len(f[0])) if f[i][x] == 'S'] for i in range(len(f)) if 'S' in f[i]][0][0]
len_f = len([0 for i in range(len(f)) for x in range(len(f[0])) if f[i][x] != '#'])
possible = {(0, 0): {start}}
axes = [(1, 0), (0, 1), (-1, 0), (0, -1)]
p = {(x, y): {((x + axe[0] + len(f[0])) % len(f[0]), (y + axe[1] + len(f)) % len(f)): (-1 if x + axe[0] < 0 else 1 if x + axe[0] >= len(f[0]) else 0, -1 if y + axe[1] < 0 else 1 if y + axe[1] >= len(f) else 0) for axe in axes if f[(y + axe[1] + len(f)) % len(f)][(x + axe[0] + len(f[0])) % len(f[0])] != '#'} for y in range(len(f)) for x in range(len(f[0]))}
blocked = {(x, i): any(f[z[1]][z[0]] != '#' for z in p[(x, i)]) for i in range(len(f)) for x in range(len(f[0]))}
steps = 26501365
devs = (steps * 2 + 1) // w - 2
countings = {z: sum([len([0 for x in range((i + z) % 2, w, 2) if f[i][x] != '#'  and any(f[z[1]][z[0]] != '#' for z in p[(x, i)])]) for i in range(h)]) for z in range(2)}
counter = 2 * ((devs // 2) * (devs // 2 + 1) / 2 * countings[0] + (devs // 2 - 1) * (devs // 2) / 2 * countings[1]) + (devs // 2) * countings[1] + (devs // 2 + 1) * countings[0]
print(counter)


def part1(st, s):
    possible = [st]
    axes = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(s):
        new = []
        for p in possible:
            for axe in axes:
                x, y = p[0] + axe[0], p[1] + axe[1]
                if 0 <= x < len(f[0]) and 0 <= y < len(f) and f[y][x] != '#' and (x, y) not in new:
                    new.append((x, y))
        possible = new.copy()
    return len(possible)

multipliers = [[1, (w // 2, h - 1), w - 1], [1, (w // 2, 0), w - 1], [1, (w - 1, h // 2), w - 1], [1, (0, h // 2), w - 1], [steps // h, (0, 0), w // 2 - 1], [steps // h, (w - 1, h - 1), w // 2 - 1], [steps // h, (0, h - 1), w // 2 - 1], [steps // h, (w - 1, 0), w // 2 - 1], [steps // h - 1, (w - 1, 0), w // 2 - 1 + w], [steps // h - 1, (0, h - 1), w // 2 - 1 + w], [steps // h - 1, (0, 0), w // 2 - 1 + w], [steps // h - 1, (w - 1, h - 1), w // 2 - 1 + w], ]

for i in multipliers:
    q = i[0] * part1(i[1], i[2])
    counter += q
    print(counter, i, q)
print(counter)