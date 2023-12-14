import itertools

f = [(lambda x: [([j for j in x[0]] + ['?']) * 4 + [j for j in x[0]], [int(j) for j in x[1].split(',')] * 5])(i.split()) for i in open('input.txt', 'r').read().split('\n')]


for i in range(len(f)):
    if '#' not in f[i][0] and '.' not in f[i][0]:
        print(i+1)
