f = [[int(x) for x in i.split(':')[1].split()] for i in open('input.txt', 'r').read().split('\n')]
c = 1

for i in range(len(f[0])):
    c *= sum([1 for x in range(f[0][i]) if (f[0][i] - x) * x > f[1][i]])

print(c)