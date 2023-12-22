f = [(lambda x: [''.join(([j for j in x[0]] + ['?']) * 4 + [j for j in x[0]]), [int(j) for j in x[1].split(',')] * 5])(i.split()) for i in open('input.txt', 'r').read().split('\n')]
c = 0


def getFixed(x):
    a, p, b = {}, 0, 0
    for i in range(len(x)):
        if x[i] == '#':
            if p == 0:
                b = i
            p += 1
        if p != 0 and x[i] != '#':
            a[b] = p
            p = 0
    if p != 0:
        a[b] = p
    return a

def isHigher(x, y):
    for i in x:
        if i >= y:
            return True
    return False

def isPossible(line, pos, following, line_len):
    return (pos == 0 or line[pos-1] != '#') and (line_len == pos + following or line[pos+following] != '#') and all([line[i] in ['?', '#'] for i in range(pos, pos+following)])

def findCombinations(pos, left, line, line_len, fixed):
    global data
    if left == []:
        if not isHigher(fixed, pos):
            return 1
        return 0
    else:
        summary = 0
        for i in range(pos, line_len - sum(left) - len(left) + 2):
            value = fixed.get(i)
            if value is not None:
                if value <= left[0] and all([line[x] in ['?', '#'] for x in range(i, i+left[0])]) and (i + left[0] == line_len or line[i+left[0]] != '#'):
                    con = data.get((i, len(left)))
                    if con is not None:
                        summary += con
                    else:
                        s = findCombinations(i + left[0] + 1, left[1:], line, line_len, fixed)
                        summary += s
                        data.update({(i, len(left)): s})
                break
            if isPossible(line, i, left[0], line_len):
                con = data.get((i, len(left)))
                if con is not None:
                    summary += con
                else:
                    s = findCombinations(i + left[0] + 1, left[1:], line, line_len, fixed)
                    summary += s
                    data.update({(i, len(left)): s})
        return summary

for idx, i in enumerate(f, start=1):
    data = {}
    cg = findCombinations(0, i[1], i[0], len(i[0]), getFixed(i[0]))

    c += cg

print(c)

#final version
