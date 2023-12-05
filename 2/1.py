f = [[[(lambda j: [int(j[0]), j[1]])(y.split()) for y in z.split(', ')] for z in i.split(': ')[1].split('; ')] for i in open('input.txt', 'r').read().split('\n')]
c = 0

for i in range(len(f)):
    for x in f[i]:
        a = {'red': 12, 'green': 13, 'blue': 14}
        for j in x:
            a[j[1]] -= j[0]
            if a[j[1]] < 0:
                break
        else:
            continue
        break
    else:
        c += i + 1
print(c)
