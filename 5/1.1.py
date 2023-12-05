f = [i for i in open('input.txt', 'r').read().split('\n\n')]
a = [int(i) for i in f[0].split(': ')[1].split()]
f = [(lambda y: [x for x in y[0][:-5].split('-to-')] + [[int(z) for z in x.split()] for x in y[1:]])(i.split('\n')) for i in f[1:]]
fd = {(i[0], i[1]): i[2:] for i in f}
fg = {}
for i, x in fd.keys():
    if i in fg:
        fg[i].append(x)
    else:
        fg[i] = [x]
    if x in fg:
        fg[x].append(i)
    else:
        fg[x] = [i]
print(a, fd)

best_ = 999999999999999999999

for i in range(len(a)):
    p = [('seed', a[i])]
    best = 999999999999999999999
    while best == 999999999999999999999:
        new = []
        for x in p:
            for z in fg[x[0]]:
                if (x[0], z) in fd:
                    for y in fd[(x[0], z)]:
                        if y[1] <= x[1] < y[1] + y[2]:
                            if z == 'location':
                                if best > x[1] - y[1] + y[0]:
                                    best = x[1] - y[1] + y[0]
                            else:
                                new.append((z, x[1] - y[1] + y[0]))

                            break
                    else:
                        if z == 'location':
                            if best > x[1]:
                                best = x[1]
                        else:
                            new.append((z, x[1]))
        p = new.copy()
        
    if best_ > best:
        best_ = best
print(best_)