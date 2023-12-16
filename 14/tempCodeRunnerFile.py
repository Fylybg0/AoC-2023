with open('vstup3.txt', 'r') as subor:
    text = subor.read()
    riadky = text.split('\n')
    C = []
    for riadok in riadky:
        prvky = riadok.split()
        C.append([])
        for prvok in prvky:
            C[-1].append(prvok)
    
print('pred')
for riadok in C:
    print(riadok)

for i in range(len(C)):
    C[0][i], C[i][0] = C[i][0], C[0][i]

print('po')
for riadok in C:
    print(riadok)