f = [(lambda x: [x[0]] + [[i for i in x[1].split()]])(i.split(': ')) for i in open('input.txt', 'r').read().strip().split('\n')]
start = f[0][0]
graph = {}
for node in f:
    for node_ in node[1]:
        if node[0] in graph:
            graph[node[0]].append(node_)
        else:
            graph[node[0]] = [node_]
        if node_ in graph:
            graph[node_].append(node[0])
        else:
            graph[node_] = [node[0]]
conections = [(i[0], x) for idx, i in enumerate(f) for x in f[idx][1]]
nodes = set([i for i in graph] + [x for i in graph for x in graph[i]])
lenght = len(nodes)

def devide(c):
    cycle = [c]
    conections = graph[c].copy()
    while len(cycle) != lenght and len(conections) != 3:
        cycle.append(conections[0])
        conections = [node for node in conections if node != conections[0]] + [node for node in graph[conections[0]] if node not in cycle]
        
    return len(cycle)

for idx, node in enumerate(nodes):
    print(idx, node)
    cycle_lenght = devide(node)
    if cycle_lenght != lenght:
        print(cycle_lenght * (lenght - cycle_lenght))
        break