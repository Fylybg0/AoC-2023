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

def isInd(x):
    return sum([len([0 for z in graph[i] if z not in x]) for i in x]) <= 3


def devide():
    possible = {(start, )}
    while True:
        print(len(possible))
        new = set()
        for p in possible:
            for con in p:
                for node in graph[con]:
                    if node not in p:
                        for idx, i in enumerate(p):
                            if i > node:
                                new_con = p[:idx] + (node, ) + p[idx:]
                                break
                        else:
                            new_con = p + (node, )
                        if isInd(new_con):
                            return len(new_con)
                        new.add(new_con)
        possible = new.copy()

dev = devide()
print(dev)
print(dev * (lenght - dev))