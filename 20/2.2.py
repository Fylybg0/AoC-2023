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

def makeCycle(x):
    print([f[i][1] == '%' for i in conjunctions[conjunctions[x][0]] + [i for i in f[conjunctions[x][0]][0] if i != x]])
    return conjunctions[conjunctions[x][0]].copy() + [i for i in f[conjunctions[x][0]][0] if i != x]

cycles = {i: makeCycle(i) for i in conjunctions[conjunctions['rx'][0]]}
cycles_final_idexes = {i: 0 for i in cycles}
xxxx = {i: [] for i in cycles}


def isCon(x):
    return not all([not(f[i][2]) if f[i][1] == '%' else isCon(i) for i in conjunctions[x]])

pressed_counter = 0
#while pressed_counter < 10000 and pressed_counter < 3785:
while any(cycles_final_idexes[i] == 0 for i in cycles_final_idexes) and pressed_counter < 10000:
    pressed_counter += 1
    if pressed_counter % 1000 == 0:
        print(pressed_counter, cycles_final_idexes)
    #print(pressed_counter)

    states = [('broadcaster', 'low')]
    while states != []:
        new = []
        for state in states:
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

    for i in cycles_final_idexes:
        #if cycles_final_idexes[i] == 0:
        if all([not(f[i][2]) for i in cycles[i]]):
            if cycles_final_idexes[i] == 0:
                cycles_final_idexes[i] = pressed_counter
            xxxx[i].append(pressed_counter)
    
    #print(cycles_cycles)
    #print(f)
#print(math.lcm(*[cycles_final_idexes[i][1]-1 for i in cycles_final_idexes]))

print(cycles_final_idexes)
print(math.lcm(*[cycles_final_idexes[i]-1 for i in cycles_final_idexes]))
#print(xxxx)

#1193111905160 too low
#76463729393559 too low
#25476397365272
#77503163177664 too low
#2421963944232
#98928086739685
#76463729393559
#99181271497765
#71764039406345
#102254373122825
#11866187199867
#232605773145467