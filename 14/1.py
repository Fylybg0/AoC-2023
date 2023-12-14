f = [i for i in open('input.txt', 'r').read().split('\n')]
rounded_rocks = []
cubed_rocks = []
new = []

for i in range(len(f)):
    for x in range(len(f[0])):
        if f[i][x] == 'O':
            rounded_rocks.append((x, i))
        elif f[i][x] == '#':
            cubed_rocks.append((x, i))

for i in range(len(rounded_rocks)):
    x, y = rounded_rocks[i]
    for j in range(y, -1, -1):
        if (x, j) in cubed_rocks or (x, j) in new:
            new.append((x, j+1))
            break
    else:
        new.append((x, 0))
rounded_rocks = new.copy()
new = []

for i in range(len(f)):
    print(''.join(['O' if (x, i) in rounded_rocks else '#' if (x, i) in cubed_rocks else '.' for x in range(len(f[0]))]))
print()
print(sum(len(f) - y for x, y in new))

