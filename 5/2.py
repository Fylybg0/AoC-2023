f = [i for i in open('input.txt', 'r').read().split('\n\n')]
a = (lambda y: [(int(y[i]), int(y[i]) + int(y[i+1]) - 1) for i in range(0, len(y), 2)])(f[0].split(': ')[1].split())
f = [(lambda y: [x for x in y[0][:-5].split('-to-')] + [[int(z) for z in x.split()] for x in y[1:]])(i.split('\n')) for i in f[1:]]
fd = {(i[0], i[1]): i[2:] for i in f}
fg = {i: x for i, x in fd.keys()}

best = float('inf')

def overlap(x, y):      
    if (x[1] >= y[1] and x[0] <= y[0]):
        return y, ([(x[0], y[0]-1)] if x[0] != y[0] else []) + ([(y[1]+1, x[1])] if y[1] != x[1] else [])
    elif (x[0] >= y[0] and x[1] <= y[1]):
        return x, []
    elif (x[0] <= y[0] <= x[1] and x[1] <= y[1]):
        return (y[0], x[1]), [(x[0], y[0] - 1)] if x[0] != y[0] else []
    elif (x[0] >= y[0] and x[0] <= y[1] <= x[1]):
        return (x[0], y[1]), [(y[1] + 1, x[1])]  if x[1] != y[1] else []

for i in range(len(a)):
    current = 'seed'
    ranges = [a[i]]
    while current != 'location':
        new = []
        while ranges != []:
            for y in fd[(current, fg[current])]:
                over = overlap(ranges[0], (y[1], y[1] + y[2] - 1))
                if over != None:
                    new.append((over[0][0] - y[1] + y[0], over[0][1] - y[1] + y[0]))
                    ranges += over[1].copy()
                    ranges.pop(0)
                    break
            else:
                new += [ranges[0]]
                ranges.pop(0)
        current = fg[current]
        ranges = new.copy()
        
    best = min(best, min(ranges, key=lambda x: x[0])[0])

print(best)