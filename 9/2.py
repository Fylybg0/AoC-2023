f = [[int(x) for x in i.split()][::-1] for i in open('input.txt', 'r').read().split('\n')]

c = 0

for i in f:
    l = [i.copy()]
    idx = 0
    while not all(x == 0 for x in l[-1]):
        l.append([l[-1][x] - l[-1][x+1]  for x in range(len(l[-1])-1)])
    
    s = 0
    for i in range(len(l)-1):
        s = -s + l[-i-2][-1] 
    c += s

print(c) 
