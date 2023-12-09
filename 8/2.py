import math

a, f = (lambda y: [y[0], [(lambda z: list([z[0]] + [y for y in z[1][1:-1].split(', ')]))(i.split(' = ')) for i in y[1].split('\n')]])(open('input.txt', 'r').read().split('\n\n'))
cur = [i[0] for i in f if i[0][-1] == 'A']
f = {i[0]: (i[1], i[2]) for i in f}
b = {'L': 0, 'R': 1}
cur_c = [[] for i in cur]
p = [0 for i in cur]
print(len(a))
idx = 0
print(cur)
while not all([i[-1] == 'Z' for i in cur]) and p.count(0) != 0:
    for x in range(len(cur)):
        cur[x] = f[cur[x]][b[a[idx % len(a)]]]
        if cur[x][-1] == 'Z':
            cur_c[x].append([cur[x], idx + 1, idx % len(a)])
            if [(i[0], i[2]) for i in cur_c[x]].count((cur[x], idx % len(a))) != 1:
                p[x] = cur_c[x][0][1]
    ###print(cur)
    #print(cur)
    idx = idx + 1

o = 1
for i in p:
    o *= i
print(o)
print(math.lcm(*[i for i in p]))


c = [x for x in range(86827652906, 86827652907)]
print(a, cur_c, p)

for i in c:
    for x in p:
        if i % x != 0:
            break
    else:
        print(i)
        break