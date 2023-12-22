f = [(lambda i: [i[0] if i[0] == 'broadcaster' else i[0][1:]] + [[z for z in i[1].split(', ')]] + ['' if i[0] == 'broadcaster' else i[0][0]])(x.split(' -> ')) for x in open('input.txt', 'r').read().split('\n')]
f = {i[0]: ([i[1], i[2]] + ([False] if i[2] == '%' else [[]]))  for i in f}
conjunctions = {i: [] for i in f if f[i][1] == '&'}
for i in f:
    for con in conjunctions:
        if con in f[i][0]:
            conjunctions[con].append(i)

counter = {'low': 0, 'high': 0}

def change(f, x, state):
    if x in f:
        if f[x][1] == '%':
            if state == 'low':
                f[x][2] = not(f[x][2])
        elif f[x][1] == '&':
            f[x][2].append(state == 'high')

def switch(f, x, state):
    global counter
    counter[state] += 1
    if x == 'broadcaster':
        print('button', '-low->', x)
        for i in f[x][0]:
            print(x, '-low->', i)
            change(f, i, state)
        for i in f[x][0]:
            switch(f, i, 'low')
    elif x not in f:
        return
    elif f[x][1] == '%':
        if state == 'low':
            for i in f[x][0]:
                if f[x][2]:
                    change(f, i, 'high')
                    print(x, '-high->', i)
                else:
                    print(x, '-low->', i)
                    change(f, i, 'low')
            for i in f[x][0]:
                if f[x][2]:
                    switch(f, i, 'high')
                else:
                    switch(f, i, 'low')
    elif f[x][1] == '&':
        for i in f[x][0]:
            if all(f[x][2]):
                change(f, i, 'low')
                print(x, '-low->', i)
            else:
                change(f, i, 'high')
                print(x, '-high->', i)
        for i in f[x][0]:
            if all([f[z][2] for z in conjunctions[x]]):
                switch(f, i, 'low')
            else:
                switch(f, i, 'high')

print(f)
for step in range(1):
    switch(f, 'broadcaster', 'low')
    
    for x in f:
        if f[x][1] == '&':
            f[x][2] = []
    print(f)

print(counter['high'], counter['low'])
print(counter['high'] * counter['low'])


#11498906025
#8634319400