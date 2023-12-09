f = [(lambda z: [z[0], int(z[1])])(i.split()) for i in open('input.txt', 'r').read().split('\n')]
a = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}
b = [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]

def getValue(x):
    y = {i: 0 for i in x}
    for i in x:
        y[i] += 1

    if 'J' in y.keys():
        return b.index((lambda z: [z[0] + y['J']] + z[1:] if z != [] else [5])(sorted([y[i] for i in y if i != 'J'], reverse=True)))
    return b.index(sorted(y.values(), reverse=True))

def isLower(y, x):
    i, j = getValue(y), getValue(x)
    if i == j:
        return [a[z] for z in y] > [a[z] for z in x]
    return i < j

for i in range(len(f)-1):
    for x in range(i+1, len(f)):
        if isLower(f[i][0], f[x][0]):
            f[x], f[i] = f[i], f[x]

c = 0
for i in range(len(f)):
    c += f[i][1] * (i+1)
print(c)
