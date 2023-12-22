f = [[int(x) for x in i] for i in open('input.txt', 'r').read().split('\n')]

start = (0, 0)
end = (len(f[0]) - 1, len(f) - 1)
minimals = {(start, (0, 0)): 0}
axes = [(0, 1), (1, 0), (-1, 0), (0, -1)]
axes = {(0, 0): [(0, 1), (1, 0)], (0, 1): [(1, 0), (-1, 0)], (0, -1): [(1, 0), (-1, 0)], (1, 0): [(0, 1), (0, -1)], (-1, 0): [(0, 1), (0, -1)]}
low = float('inf')

while True:
    new = {}
    for mini in minimals:
        if mini[0] != end:
            for axe in axes[mini[1]]:
                for step in range(4, 11): 
                    q, p = mini[0][0] + axe[0] * step, mini[0][1] + axe[1] * step
                    if 0 <= q < len(f[0]) and 0 <= p < len(f) and minimals[mini] + f[p][q] < low and (axe[0]*-1, axe[1]*-1) != mini[1]:
                        new_key = ((q, p), axe)
                        new_sum = sum([f[mini[0][1] + axe[1] * i][mini[0][0] + axe[0] * i] for i in range(1, step+1)])
                        if (q, p) == end and low > minimals[mini] + new_sum:
                            low = minimals[mini] + new_sum
                            print(low, 'low', mini)
                        if new_key in new:
                            new[new_key] = min([new[new_key], minimals[mini] + new_sum])
                        else:
                            new[new_key] = minimals[mini] + new_sum
        else:
            new[mini] = minimals[mini]
    minimals = new
    print(len(minimals))

    if low != float('inf') and len({x[0] for x in minimals}) == 1:
        break

out = min([minimals[i] for i in minimals])
print(low)
'''
for i in range(len(f)):
    print(''.join(['#' if (x, i) in out[1] else str(f[i][x]) for x in range(len(f[0]))]))'''


#1139
#1273