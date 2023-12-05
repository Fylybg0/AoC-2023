f = [[[int(y) for y in x.split()] for x in i.split(': ')[1].split(' | ')] for i in open('input.txt').read().split('\n')]
a = [1] * len(f)

for i in range(len(f)):
    print(a)
    s = 0
    for x in f[i][1]:
        if x in f[i][0]:
            print(f[i][0], x)
            s += 1
    if s != 0:
        for z in range(s):
            a[i+z+1] += 1 * a[i]

print(sum(a))