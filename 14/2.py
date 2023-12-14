f = [i for i in open('input.txt', 'r').read().split('\n')]
rounded_rocks = []
cubed_rocks = []
new = []
cycle = 0
cycles = []
isCounted = False

for i in range(len(f)):
    for x in range(len(f[0])):
        if f[i][x] == 'O':
            rounded_rocks.append((x, i))
        elif f[i][x] == '#':
            cubed_rocks.append((x, i))

while cycle < 1000000000:
    print(cycle)
    new = []
    for i in range(len(rounded_rocks)):
        x, y = rounded_rocks[i]
        for j in range(y, -1, -1):
            if (x, j) in cubed_rocks or (x, j) in new:
                for k in range(j+1, len(f)):
                    if not ((x, k) in cubed_rocks or (x, k) in new):
                        new.append((x, k))
                        break
                break
        else:
            for k in range(0, len(f)):
                if not ((x, k) in cubed_rocks or (x, k) in new):
                    new.append((x, k))
                    break
                
    rounded_rocks = new.copy()
    new = []
    for i in range(len(rounded_rocks)):
        x, y = rounded_rocks[i]
        for j in range(x, -1, -1):
            if (j, y) in cubed_rocks or (j, y) in new:
                for k in range(j+1, len(f[0])):
                    if not ((k, y) in cubed_rocks or (k, y) in new):
                        new.append((k, y))
                        break
                break
        else:
            for k in range(0, len(f[0])):
                if not ((k, y) in cubed_rocks or (k, y) in new):
                    new.append((k, y))
                    break

    rounded_rocks = new.copy()
    new = []
    for i in range(len(rounded_rocks)):
        x, y = rounded_rocks[i]
        for j in range(y, len(f), 1):
            if (x, j) in cubed_rocks or (x, j) in new:
                for k in range(j-1, -1, -1):
                    if not ((x, k) in cubed_rocks or (x, k) in new):
                        new.append((x, k))
                        break
                break
        else:
            for k in range(len(f)-1, -1, -1):
                if not ((x, k) in cubed_rocks or (x, k) in new):
                    new.append((x, k))
                    break

    rounded_rocks = new.copy()
    new = []
    for i in range(len(rounded_rocks)):
        x, y = rounded_rocks[i]
        for j in range(x, len(f[0]), 1):
            if (j, y) in cubed_rocks or (j, y) in new:
                for k in range(j-1, -1, -1):
                    if not ((k, y) in cubed_rocks or (k, y) in new):
                        new.append((k, y))
                        break
                break
        else:
            for k in range(len(f[0])-1, -1, -1):
                if not ((k, y) in cubed_rocks or (k, y) in new):
                    new.append((k, y))
                    break
    rounded_rocks = new.copy()

    '''for i in range(len(f)):
        print(''.join(['O' if (x, i) in rounded_rocks else '#' if (x, i) in cubed_rocks else '.' for x in range(len(f[0]))]))
    print()'''
    
    cycle += 1

    sorted_rounded_rocks = sorted(rounded_rocks)
    if sorted_rounded_rocks in cycles and not isCounted:
        idx = cycles.index(sorted_rounded_rocks) + 1
        cycle += (1000000000 - idx) // (cycle - idx) * (cycle - idx) - (cycle - idx)
        isCounted = True
    cycles.append(sorted_rounded_rocks)

#a1 + n*d < 1000000000
#7 + n*15 < 1000000000
#15n < (1000000000 - 7) // 15
#n
print(sum(len(f) - y for x, y in rounded_rocks))

