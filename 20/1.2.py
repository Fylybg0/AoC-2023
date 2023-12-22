f = [(lambda i: [i[0] if i[0] == 'broadcaster' else i[0][1:]] + [[z for z in i[1].split(', ')]] + ['' if i[0] == 'broadcaster' else i[0][0]])(x.split(' -> ')) for x in open('input.txt', 'r').read().split('\n')]
f = {i[0]: ([i[1], i[2]] + ([False] if i[2] == '%' else [[]]))  for i in f}
counter = {'low': 0, 'high': 0}

def switch(f, x, state):
    global counter
    print(x)
    counter[state] += 1
    if x == 'broadcaster':
        print('button', '-low->', x)
        for i in f[x][0]:
            print(x, '-low->', i)
            switch(f, i, 'low')
    elif x not in f:
        return
    elif f[x][1] == '%':
        if state == 'low':
            f[x][2] = not(f[x][2])
            for i in f[x][0]:
                if f[x][2]:
                    print(x, '-high->', i)
                    switch(f, i, 'high')
                else:
                    print(x, '-low->', i)
                    switch(f, i, 'low')
    elif f[x][1] == '&':
        f[x][2].append(state == 'high')
        for i in f[x][0]:
            if all(f[x][2]):
                print(x, '-low->', i)
                switch(f, i, 'low')
            else:
                print(x, '-high->', i)
                switch(f, i, 'high')

print(f)
for step in range(1):
    switch(f, 'broadcaster', 'low')
    
    for x in f:
        if f[x][1] == '&':
            f[x][2] = []
    #print(f)

print(counter['high'], counter['low'])
print(counter['high'] * counter['low'])


#11498906025
#11498906025