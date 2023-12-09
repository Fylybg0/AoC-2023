a = 'LLRRRLRLLRRLLRLRLRLRRLRRRLRRRLRLRRLLRLLRRRLRRLRRRLRLRRRLRRLRLRRRLRRRLRRLRLRRRLRRLRRLRRRLRLRLLRLLRLLRLRRRLRRLRRLRRRLRLRRRLRLRLRLRRRLRRRLRLRLRLRRRLRLLRRLLRLLRRLRRRLLRRRLLRRLRLRRLRLLRLLLLRRLLRRLRRLRLLLRRRLRRLRRRLRRLLRLRRRLRLLRRRLLLLRLRRRLRLRRLRRLRRLLRLRLRRLLLRRLLRLRRLRRRR'
#a = 'RL'
f = [(lambda z: list([z[0]] + [y for y in z[1][1:-1].split(', ')]))(i.split(' = ')) for i in open('input.txt', 'r').read().split('\n')]
start, end = 'AAA', 'ZZZ'
f = {i[0]: (i[1], i[2]) for i in f}
b = {'L': 0, 'R': 1}
cur = start

idx = 0

while cur != end:
    cur = f[cur][b[a[idx % len(a)]]]
    #print(cur)
    idx = idx + 1

print(idx)