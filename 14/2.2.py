f = [i for i in open('input.txt', 'r').read().split('\n')]
rounded_rocks = []
cubed_rocks = []

for i in range(len(f)):
    for x in range(len(f[0])):
        if f[i][x] == 'O':
            rounded_rocks.append((x, i))
        elif f[i][x] == '#':
            cubed_rocks.append((x, i))

for cycle in range(10):
    new = []
    for i in range(len(rounded_rocks)):
        x, y = rounded_rocks[i]
        minimal = max(min(rounded_rocks, key=lambda x: x[1])[1], min(cubed_rocks, key=lambda x: x[1])[1])
        new.append((x, minimal + 1))
    rounded_rocks = new.copy()
    new = []
    for i in range(len(f)):
        print(''.join(['O' if (x, i) in rounded_rocks else '#' if (x, i) in cubed_rocks else '.' for x in range(len(f[0]))]))
    print()
    
    for i in range(len(rounded_rocks)):
        x, y = rounded_rocks[i]
        minimal = max(min(rounded_rocks, key=lambda x: x[0])[0], min(cubed_rocks, key=lambda x: x[0])[0])
        new.append((x, minimal + 1))
    rounded_rocks = new.copy()
    new = []
    for i in range(len(f)):
        print(''.join(['O' if (x, i) in rounded_rocks else '#' if (x, i) in cubed_rocks else '.' for x in range(len(f[0]))]))
    print()
    
    for i in range(len(rounded_rocks)):
        x, y = rounded_rocks[i]
        minimal = min(max(rounded_rocks, key=lambda x: x[1])[1], max(cubed_rocks, key=lambda x: x[1])[1])
        new.append((x, minimal - 1))
    rounded_rocks = new.copy()
    new = []
    for i in range(len(f)):
        print(''.join(['O' if (x, i) in rounded_rocks else '#' if (x, i) in cubed_rocks else '.' for x in range(len(f[0]))]))
    print()
    
    for i in range(len(rounded_rocks)):
        x, y = rounded_rocks[i]
        minimal = min(max(rounded_rocks, key=lambda x: x[0])[0], max(cubed_rocks, key=lambda x: x[0])[0])
        new.append((x, minimal - 1))
    rounded_rocks = new.copy()
    for i in range(len(f)):
        print(''.join(['O' if (x, i) in rounded_rocks else '#' if (x, i) in cubed_rocks else '.' for x in range(len(f[0]))]))
    print()


print(sum(len(f) - y for x, y in new))

