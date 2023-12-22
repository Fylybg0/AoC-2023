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
    return [i for i in conjunctions[conjunctions[x][0]]]

cycles = {i: makeCycle(i) for i in conjunctions[conjunctions['rx'][0]]}
cycles_idexes = {i: tuple() for i in cycles}
cycles_final_idexes = {i: tuple() for i in cycles}

def isCon(x):
    return not all([not(f[i][2]) if f[i][1] == '%' else isCon(i) for i in conjunctions[x]])

pressed_counter = 0
while any(len(cycles_idexes[i]) < 15 and cycles_final_idexes[i] == tuple() for i in cycles_final_idexes):
    
#while any(cycles_final_idexes[i] == 0 for i in cycles_final_idexes):
    pressed_counter += 1
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
                
                    #if cycles_final_idexes[i] == 0:
                if state[0] in cycles_idexes and len(cycles_idexes[state[0]]) < 15 and cycles_final_idexes[state[0]] == tuple() and pressed_counter not in cycles_idexes[state[0]]:
                    if f[state[0]][2]:
                        cycles_idexes[state[0]] += (pressed_counter, )
                        cyc = cycles_idexes[state[0]][len(cycles_idexes[state[0]])//3] - cycles_idexes[state[0]][0]
                        first = cycles_idexes[state[0]][:len(cycles_idexes[state[0]])//3]
                        second = tuple(z - cyc for z in cycles_idexes[state[0]][len(cycles_idexes[state[0]])//3:len(cycles_idexes[state[0]])//3*2])
                        third = tuple(z - cyc * 2 for z in cycles_idexes[state[0]][len(cycles_idexes[state[0]])//3*2:])
                        #print(state[0], cycles_idexes[state[0]][:len(cycles_idexes[state[0]])//2], tuple(z - cycles_idexes[state[0]][0] for z in cycles_idexes[state[0]i][len(cycles_idexes[state[0]])//2:]), cycles_idexes[state[0]][:len(cycles_idexes[state[0]])//2] == tuple(z - cycles_idexes[state[0]][0] for z in cycles_idexes[state[0]][len(cycles_idexes[state[0]])//2:]))
                        if len(cycles_idexes[state[0]]) % 3 == 0 and cyc >= cycles_idexes[state[0]][0] and first == second == third:
                            cycles_final_idexes[state[0]] = (cycles_idexes[state[0]][len(cycles_idexes[state[0]])//3-1], cyc)
                            print(state[0], cycles_final_idexes[state[0]])
                            #print(cycles_idexes[i])
        states = new.copy()

    
    #print(cycles_cycles)
    #print(f)
print(cycles_idexes)
#print(math.lcm(*[cycles_final_idexes[i][1] for i in cycles_final_idexes]))
print(math.lcm(2828, 3151, 4074, 3736))
my = cycles_final_idexes['ph'][1] * cycles_final_idexes['tx'][1]
k = 0

while True:
    if k % cycles_final_idexes['dd'][1] == cycles_final_idexes['dd'][0] and k % cycles_final_idexes['nz'][1] == cycles_final_idexes['nz'][0]:
        print(k)
        break
    k += my  


#1193111905160 too low
#76463729393559 too low
#25476397365272
#77503163177664 too low
#2421963944232