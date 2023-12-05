f = [i for i in open('input.txt', 'r').read().split()]
axes = [(-1 , -1), (0 , -1), (1 , -1), (-1 , 0), (1 , 0), (-1 , 1), (0 , 1), (1 , 1)]

c = 0

def find_number(x, y, turn = None):
    if not 0 <= x < len(f[0]) or not f[y][x].isnumeric():
        return ''
    return find_number(x-1, y, 'left') + f[y][x] + find_number(x+1, y, 'right') if turn == None else (find_number(x-1, y, 'left') + f[y][x] if turn == 'left' else f[y][x] + find_number(x+1, y, 'right'))

def find_pos(x, y, turn = None):
    if not 0 <= x < len(f[0]) or not f[y][x].isnumeric():
        return []
    return find_pos(x-1, y, 'left') + [(x, y)] + find_pos(x+1, y, 'right') if turn == None else find_pos(x-1, y, 'left') + [(x, y)] if turn == 'left' else [(x, y)] + find_pos(x+1, y, 'right')


for y in range(len(f)):
    for x in range(len(f[0])):
        if f[y][x] == '*':
            visited = []
            numbers = []

            for axe in axes:
                p, q = y + axe[1], x + axe[0]
                if 0 <= q < len(f[0]) and 0 <= p < len(f) and f[p][q].isnumeric() and (q, p) not in visited:
                    numbers.append(int(find_number(q, p)))
                    visited += find_pos(q, p).copy()
                    
            if len(numbers) == 2:
                c += numbers[0] * numbers[1]
            
            



print(c)