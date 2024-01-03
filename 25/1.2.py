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

def findCycle(st):
    possible = {(st, )}
    while True:
        new = set()
        for p in possible:
            for node in graph[p[-1]]:
                if node not in p:
                    new.add(p + (node, ))
                if (len(p) >= 3 and p[0] == node):
                    return p
        possible = new.copy()

def findExtendConnection(conections):
    for node in conections:
        for node_ in conections:
            if node_ != node:
                if node in graph[node_] or node_ in graph[node]:
                    return [node, node_]

def devide(c):
    cycle = c
    print(len(c))
    while len(cycle) != lenght:
        if len(cycle) % 300 == 0:
            print(len(cycle))
        conections = [node for con in cycle for node in graph[con] if node not in cycle]
        if len(conections) == 3:
            print(conections)
            return len(cycle)
        nodes = max([[node_ for node_ in graph[node] if node_ not in cycle] for node in cycle], key = len)      
        cycle += nodes.copy()
    return lenght

for node in nodes:
    print(node)
    cycle_lenght = devide(list(findCycle(node)))
    if cycle_lenght != lenght:
        print(cycle_lenght * (lenght - cycle_lenght))
        break