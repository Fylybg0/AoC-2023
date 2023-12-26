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

def devide(x):
    visited = [start]
    possible = [start]
    while possible != []:
        new = []
        for p in possible:
            for node in graph[p]:
                if node not in visited and (p, node) not in x and (node, p) not in x:
                    visited.append(node)
                    if node in graph:
                        new.append(node)
        possible = new.copy()
    return len(visited)

def findNumber():
    for i in range(len(conections) - 2):
        #print('i:', i)
        for j in range(i + 1, len(conections) - 1):
            print('j:', j)
            for x in range(j + 1, len(conections)):
                #print('x:', x)
                dev = devide([conections[i], conections[j], conections[x]])
                if dev != lenght and dev != 1:
                    return dev * (lenght - dev)

print(findNumber())