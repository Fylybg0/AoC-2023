import math

f = [(lambda i: [i[0] if i[0] == 'broadcaster' else i[0][1:]] + [[z for z in i[1].split(', ')]] + ['' if i[0] == 'broadcaster' else i[0][0]])(x.split(' -> ')) for x in open('input.txt', 'r').read().split('\n')]
f = {i[0]: [i[1], i[2], False] for i in f}
f.update({'rx': [[], '%', False]})
start_f = {i: [f[i][0].copy(), f[i][1], f[i][2]] for i in f}

conjunctions = {i: [] for i in f if f[i][1] == '&' or i == 'rx'}
for i in f:
    for con in conjunctions:
        if con in f[i][0]:
            conjunctions[con].append(i)


def isCon(x):
    return not all([not(f[i][2]) if f[i][1] == '%' else isCon(i) for i in conjunctions[x]])
s = []

for i in f['broadcaster'][0]:
    current = i
    a = ''
    while True:
        for x in f[current][0]:
            if f[x][1] == '%':
                a += '0' if len(f[current][0]) == 1 else '1'
                current = x
                break
            else:
                if len(f[current][0]) == 1:
                    a += '1'
        else:
            break
    s.append(int(a[::-1], 2))
    print(a[::-1])

    
    #print(cycles_cycles)
    #print(f)
#print(math.lcm(*[cycles_final_idexes[i][1] for i in cycles_final_idexes]))
print(s)
print(math.lcm(*s))

#1193111905160 too low
#76463729393559 too low
#25476397365272
#77503163177664 too low
#2421963944232
#98928086739685
#389452852698