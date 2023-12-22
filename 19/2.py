#plan, parts = (lambda y: tuple([y[0]] + [[(lambda f: [[f[0][0], f[0][1], int(f[0][2:])]] + [f[1].split()](j.split(':'))]])[(z.split('{')) for z in x[0].split('\n')]))(open('input.txt', 'r').read().split('\n\n'))
plan, parts = open('input.txt', 'r').read().split('\n\n')
plan = [(lambda x: {x[0]: x[1][:-1]})(i.split('{')) for i in plan.split('\n')]
plans = {}
for i in plan:
    plans.update(i)
parts = [{x[0]: int(x[2:]) for x in i[1:-1].split(',')} for i in parts.split('\n')]
combinations = {'x': set(), 'm': set(), 'a': set(), 's': set(), }
def_part = {'x': {i for i in range(1, 4001)}, 'm': {i for i in range(1, 4001)}, 'a': {i for i in range(1, 4001)}, 's': {i for i in range(1, 4001)}}
upper_lower = {'>': lambda x, y: x > y, '<': lambda x, y: x < y}

def getAnswer(possible, plan):
    double_dot, line = plan.index(':'), plan.index(',')
    condition = [plan[0], plan[1], int(plan[2:double_dot])]
    out = [plan[double_dot + 1:line], plan[line+1:]]
    true = set()
    false = set()
    c = 0

    for num in possible[condition[0]]:
        if upper_lower[condition[1]](num, condition[2]):
            true.add(num)
        else:
            false.add(num)

    if out[0] == 'R':
        pass
    elif out[0] == 'A':
        print([len(possible[i]) if condition[0] != i else len(true) for i in possible])
        cc = 1
        for i in possible:
            cc *= len(possible[i]) if condition[0] != i else len(true)
        c += cc
    elif out[0] not in plans:
        c += getAnswer({i: (possible[i] if i != condition[0] else true) for i in possible}, out[0])
    else:
        c += getAnswer({i: (possible[i] if i != condition[0] else true) for i in possible}, plans[out[0]])

    if out[1] == 'R':
        pass
    elif out[1] == 'A':
        print([len(possible[i]) if condition[0] != i else len(false) for i in possible])
        cc = 1
        for i in possible:
            cc *= len(possible[i]) if condition[0] != i else len(false)
        c += cc
    elif out[1] not in plans:
        c += getAnswer({i: (possible[i] if i != condition[0] else false) for i in possible}, out[1])
    else:
        c += getAnswer({i: (possible[i] if i != condition[0] else false) for i in possible}, plans[out[1]])

    return c

def_part = getAnswer(def_part, plans['in'])


print(def_part)

#255808047996000
#167409079868000
#167267608266850
#14285065632552