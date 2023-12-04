f  = [i.strip() for i in open('input.txt', 'r').readlines()]

c = 0
for idx, i in enumerate(f):
    n = min([(i.index(str(x)), x) for x in range(10) if str(x) in i], key= lambda x: x[0])
    m = min([(i[::-1].index(str(x)), x) for x in range(10) if str(x) in i[::-1]], key= lambda x: x[0])
    
    c += int(str(n[1])+str(m[1]))
print(c)