f = [int(''.join([x for x in i.split(':')[1].split()])) for i in open('input.txt', 'r').read().split('\n')]
c = 1

for i in range(1):
    c *= sum([1 for x in range(f[0]) if (f[0] - x) * x > f[1]])

print(c)

print((lambda f: sum([1 for x in range(f[0]) if (f[0] - x) * x > f[1]]))([int(''.join([x for x in i.split(':')[1].split()])) for i in open('input.txt', 'r').read().split('\n')]))
