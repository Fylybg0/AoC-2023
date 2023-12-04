f = [[[(lambda j: [int(j[0]), j[1]])(y.split()) for y in z.split(', ')] for z in i.split(': ')[1].split('; ')] for i in open('input.txt', 'r').read().split('\n')]
c = 0

for i in range(len(f)):
    a = {'red': 0, 'green': 0, 'blue': 0}
    for x in f[i]:
        for j in x:
            if j[0] > a[j[1]]:
                a[j[1]] = j[0]
    c += a['red'] * a['green'] * a['blue']

print(c)
