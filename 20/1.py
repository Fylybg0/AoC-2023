f = [(lambda i: [i[0] if i[0] == 'broadcaster' else i[0][1:]] + [[z for z in i[1].split(', ')]] + ['' if i[0] == 'broadcaster' else i[0][0]])(x.split(' -> ')) for x in open('input.txt', 'r').read().split('\n')]
f = {i[0]: [i[1], i[2], False]  for i in f}
conjunctions = {i: [] for i in f if f[i][1] == '&'}
for i in f:
    for con in conjunctions:
        if con in f[i][0]:
            conjunctions[con].append(i)
counter = {'low': 0, 'high': 0}

def isCon(x):
    return not all([f[i][2] if f[i][1] == '%' else isCon(i) for i in conjunctions[x]])

for step in range(1000):
    states = [('broadcaster', 'low')]
    while states != []:
        new = []
        for state in states:
            counter[state[1]] += 1
            if state[0] in f:
                for i in f[state[0]][0]:
                    if state[0] == 'broadcaster':
                        new.append((i, 'low'))
                    elif f[state[0]][1] == '%':
                        if state[1] == 'low':
                            new.append((i, 'low' if f[state[0]][2] else 'high'))
                    elif f[state[0]][1] == '&':
                        new.append((i, 'high' if isCon(state[0]) else 'low'))
                if f[state[0]][1] == '%':
                    if state[1] == 'low':
                        f[state[0]][2] = not(f[state[0]][2])
                elif f[state[0]][1] == '&':
                    f[state[0]][2] = isCon(state[0])
        states = new.copy()
    #print(f)

print(counter['high'], counter['low'])
print(counter['high'] * counter['low'])