f  = [i.strip() for i in open('input.txt', 'r').readlines()]
a = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
p = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

c = 0
for idx, i in enumerate(f):
    n = min([(i.index(str(x)), x) for x in range(10) if str(x) in i] + [(i.index(x), a[x]) for x in p if x in i], key = lambda x: x[0])
    m = min([(i[::-1].index(str(x)), x) for x in range(10) if str(x) in i[::-1]] + [(i[::-1].index(x[::-1]), a[x]) for x in p if x[::-1] in i[::-1]], key= lambda x: x[0])
    
    
    c += int(str(n[1])+str(m[1]))
print(c)