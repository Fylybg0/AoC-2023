f = [[[int(y) for y in x.split()] for x in i.split(': ')[1].split(' | ')] for i in open('input.txt').read().split('\n')]
c = 0

for i in f:
    s = 0
    for x in i[1]:
        if x in i[0]:
            s += 1
    if s != 0:
        c += 2 ** (s - 1)

print(c)