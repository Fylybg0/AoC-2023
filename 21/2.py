f = [i for i in open('input.txt', 'r').read().split('\n')]
w, h = len(f[0]), len(f)
start = [[(x, i) for x in range(len(f[0])) if f[i][x] == 'S'] for i in range(len(f)) if 'S' in f[i]][0][0]
len_f = len([0 for i in range(len(f)) for x in range(len(f[0])) if f[i][x] != '#'])
possible = {(0, 0): {start}}
axes = [(1, 0), (0, 1), (-1, 0), (0, -1)]
p = {(x, y): {((x + axe[0] + len(f[0])) % len(f[0]), (y + axe[1] + len(f)) % len(f)): (-1 if x + axe[0] < 0 else 1 if x + axe[0] >= len(f[0]) else 0, -1 if y + axe[1] < 0 else 1 if y + axe[1] >= len(f) else 0) for axe in axes if f[(y + axe[1] + len(f)) % len(f)][(x + axe[0] + len(f[0])) % len(f[0])] != '#'} for y in range(len(f)) for x in range(len(f[0]))}
blocked = {(x, i): any(f[z[1]][z[0]] != '#' for z in p[(x, i)]) for i in range(len(f)) for x in range(len(f[0]))}
steps = 26501365
counter = (steps + 1) * 2   #  // 4 * 8
countings = {i: {0: len([0 for x in range(0, len(f[0]), 2) if f[i][x] != '#' and blocked[(x, i)]]), 1: len([0 for x in range(1, len(f[0]), 2) if f[i][x] != '#' and any(f[z[1]][z[0]] != '#' for z in p[(x, i)])])} for i in range(len(f))}
print(counter)
blocks = []

cou = (steps * (steps + 1)) // 2 + ((steps + 1) * (steps + 2)) / 2 
print(cou)
data = {}
for i in range(1, steps):
    xs = steps - i
    y = (start[1] - i) % h

    t = xs // (w * 2)
    counter += t * (countings[y][0] + countings[y][1])
    xs -= t * w * 2
    if xs >= start[0] + w:
        counter += countings[y][0 if y % 2 == 1 else 1]
        xs -= w
    if (start[0] - (1 if y % 2 == 0 else 2), (-xs + start[0] if xs > start[0] else xs) - 1, -2) in data:
        c = data[(start[0] - (1 if y % 2 == 0 else 2), (-xs + start[0] if xs > start[0] else xs) - 1, -2)]
    else:
        c = 0
        for j in range(start[0] - (1 if y % 2 == 1 else 2), ((-xs + start[0]) if xs > start[0] else (start[0] - xs)) - 2, -2):
            if f[y][(j + w) % w] != '#' and blocked[((j + w) % w, y)]:
                c += 1
        #data[(start[0] - (1 if y % 2 == 1 else 2), (-xs + start[0] if xs > start[0] else xs) - 1, -2)] = c
    counter += c
print(counter)
for i in range(1, steps):
    xs = steps - i
    y = (start[1] - i) % h

    t = xs // (w * 2)
    counter += t * (countings[y][0] + countings[y][1])
    xs -= t * w * 2
    if xs >= start[0] + w:
        counter += countings[y][0 if y % 2 == 1 else 1]
        xs -= w
    if (start[0] + (1 if y % 2 == 0 else 2), xs + 1 - (start[0] if xs > start[0] else 0), 2) in data:
        c = data[(start[0] + (1 if y % 2 == 0 else 2), xs + 1 - (start[0] if xs > start[0] else 0), 2)]
    else:
        c = 0
        for j in range(start[0] + (1 if y % 2 == 1 else 2), start[0] + xs + 2 - (start[0] if xs > start[0] else 0), 2):
            if f[y][(j + w) % w] != '#' and blocked[((j + w) % w, y)]:
                c += 1
        #data[(start[0] + (1 if y % 2 == 1 else 2), xs + 1 - (start[0] if xs > start[0] else 0), 2)] = c
    counter += c
        
print(counter)
for i in range(1, steps):
    xs = steps - i
    y = (start[1] + i) % h

    t = xs // (w * 2)
    counter += t * (countings[y][0] + countings[y][1])
    xs -= t * w * 2
    if xs >= start[0] + w:
        counter += countings[y][0 if y % 2 == 1 else 1]
        xs -= w
    if (start[0] - (1 if y % 2 == 0 else 2), (-xs + start[0] if xs > start[0] else xs) - 1, -2) in data:
        c = data[(start[0] - (1 if y % 2 == 0 else 2), (-xs + start[0] if xs > start[0] else xs) - 1, -2)]
    else:
        c = 0
        for j in range(start[0] - (1 if y % 2 == 1 else 2), ((-xs + start[0]) if xs > start[0] else (start[0] - xs)) - 2, -2):
            if f[y][(j + w) % w] != '#' and blocked[((j + w) % w, y)]:
                c += 1
        #data[(start[0] - (1 if y % 2 == 1 else 2), (-xs + start[0] if xs > start[0] else xs) - 1, -2)] = c
    counter += c

print(counter)
for i in range(1, steps):
    xs = steps - i
    y = (start[1] + i) % h

    t = xs // (w * 2)
    counter += t * (countings[y][0] + countings[y][1])
    xs -= t * w * 2
    if xs >= start[0] + w:
        counter += countings[y][0 if y % 2 == 1 else 1]
        xs -= w
    if (start[0] + (1 if y % 2 == 0 else 2), xs + 1 - (start[0] if xs > start[0] else 0), 2) in data:
        c = data[(start[0] + (1 if y % 2 == 0 else 2), xs + 1 - (start[0] if xs > start[0] else 0), 2)]
    else:
        c = 0
        for j in range(start[0] + (1 if y % 2 == 1 else 2), start[0] + xs + 2 - (start[0] if xs > start[0] else 0), 2):
            if f[y][(j + w) % w] != '#' and blocked[((j + w) % w, y)]:
                c += 1
        #data[(start[0] + (1 if y % 2 == 1 else 2), xs + 1 - (start[0] if xs > start[0] else 0), 2)] = c
    counter += c
    

print(counter)
'''for i in range(len(f)):
    print(*['O' if (x, i) in blocks else '#' if f[i][x] == '#' else '.' for x in range(len(f[0]))], sep='')
'''
#628204185287090 too low
#628204185489264 too low
#175580639718537
#702322399865955
#702322399865956
#628205185561135 too low