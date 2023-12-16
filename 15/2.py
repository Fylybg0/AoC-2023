f = [i for i in open('input.txt', 'r').read().split(',')]
b = {}
c = 0

for string in f:

    if '-' in string:
        a = 0
        for i in string[:-1]:
            a = ((a + ord(i)) * 17) % 256
        if a not in b:
            b[a] = []
        
        for i in b[a]:
            if string[:-1] == i[0]:
                b[a].remove(i)
    else:
        c = string.split('=')

        a = 0
        for i in c[0]:  
            a = ((a + ord(i)) * 17) % 256
        if a not in b:
            b[a] = []
        
        for i in b[a]:
            if i[0] == c[0]:
                i[1] = int(c[1])
                break
        else:
            b[a].append([c[0], int(c[1])])
    
print(b)
c = 0
for key in b:
    for i in range(len(b[key])):
        c += (key + 1) * (i + 1) * b[key][i][1]
print(c)
