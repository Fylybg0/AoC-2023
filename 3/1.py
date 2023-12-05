f = [i for i in open('input.txt', 'r').read().split()]
axes = [(-1 , -1), (0 , -1), (1 , -1), (-1 , 0), (0 , 0), (1 , 0), (-1 , 1), (0 , 1), (0 , 1)]
visited = []
numbers = []
a = False

c = 0

def find_number(x, y, turn = 'right'):
    if not 0 <= x < len(f[0]) or not f[y][x].isnumeric():
        return ''
    return find_number(x-1, y, 'left') + f[y][x] + find_number(x+1, y, 'right') if turn == None else (find_number(x-1, y, 'left') + f[y][x] if turn == 'left' else f[y][x] + find_number(x+1, y, 'right'))

def find_pos(x, y, turn = 'right'):
    if not 0 <= x < len(f[0]) or not f[y][x].isnumeric():
        return []
    return find_pos(x-1, y, 'left') + [(x, y)] if turn == 'left' else [(x, y)] + find_pos(x+1, y, 'right')


for y in range(len(f)):
    for x in range(len(f[0])):
        if f[y][x].isnumeric() and (x, y) not in visited:
            poses = find_pos(x, y)
            print(poses)
            a = False
            for i in range(3):
                p, q = y + i - 1, x - 1
                if 0 <= p < len(f[0]) and 0 <= q < len(f):
                    if f[p][q] != '.' and not f[p][q].isnumeric():
                        a = True
                        break
            if not a:        
                for j in range(len(poses)):
                    for i in range(2):
                        p, q = poses[j][1] + (i * 2) - 1, poses[j][0]
                        if 0 <= p < len(f[0]) and 0 <= q < len(f):
                            if f[p][q] != '.' and not f[p][q].isnumeric():
                                a = True
                                break
                    else:
                        continue
                    break
                if not a:
                    for i in range(3):
                        p, q = poses[-1][1] + i - 1, poses[-1][0] + 1
                        if 0 <= p < len(f[0]) and 0 <= q < len(f):
                            if f[p][q] != '.' and not f[p][q].isnumeric():
                                a = True
                                break
            if a:
                visited += poses
                c += int(find_number(x, y))
                numbers += [int(find_number(x, y))]
            



print(numbers, c)