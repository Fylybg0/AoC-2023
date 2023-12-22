#plan, parts = (lambda y: tuple([y[0]] + [[(lambda f: [[f[0][0], f[0][1], int(f[0][2:])]] + [f[1].split()](j.split(':'))]])[(z.split('{')) for z in x[0].split('\n')]))(open('input.txt', 'r').read().split('\n\n'))
plan, parts = open('input.txt', 'r').read().split('\n\n')
plan = [(lambda x: {x[0]: x[1][:-1]})(i.split('{')) for i in plan.split('\n')]
plans = {}
for i in plan:
    plans.update(i)
parts = [{x[0]: int(x[2:]) for x in i[1:-1].split(',')} for i in parts.split('\n')]

print(parts)
print(plans)

def getAnswer(part, plan):
    double_dot, line = plan.index(':'), plan.index(',')
    condition = [plan[0], plan[1], int(plan[2:double_dot])]
    out = [plan[double_dot + 1:line], plan[line+1:]]
    w = 0 if (part[condition[0]] > condition[2] and condition[1] == '>') or (part[condition[0]] < condition[2] and condition[1] == '<') else 1
    if out[w] in ['R', 'A'] or out[w] in plans:
        return out[w]
    else:
        return getAnswer(part, out[w])

c = 0
for part in parts:
    answer = getAnswer(part, plans['in'])
    while answer not in ['R', 'A']:
        answer = getAnswer(part, plans[answer])
    
    if answer == 'A':
        c += sum([part[i] for i in part])

print(c)