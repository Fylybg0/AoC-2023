f = [[[int(z) for z in x.split(', ')] for x in i.split(' @ ')] for i in open('input.txt', 'r').read().strip().split('\n')]
mn, mx = 200000000000000, 400000000000000
#mn, mx = 7, 27       #test

def lines_intersection(x1,y1,x2,y2,vx1,vy1,vx2,vy2):
    Bx1, Bx2 = y1 + (x1 / vx1 * vy1 * -1), y2 + (x2 / vx2 * vy2 * -1) 
    '''print(vy2, (vx2 // abs(vx2)))
    print('y1 = ', vy1/vx1, '* x1 +', Bx1)
    print('y2 = ', vy2/vx2, '* x2 +', Bx2)'''
    try:
        x = (Bx2 - Bx1) / (vy1/vx1 - vy2/vx2)
        y = (vy1/vx1) * x + Bx1
    except:
        return None
    return (x, y)


counter = 0

for i in range(len(f) - 1):
    for x in range(i + 1, len(f)):
        coords = lines_intersection(f[i][0][0], f[i][0][1], f[x][0][0], f[x][0][1], f[i][1][0], f[i][1][1], f[x][1][0], f[x][1][1])
        if coords != None:
            if mn <= coords[0] <= mx and mn <= coords[1] <= mx:
                if ((f[i][0][0] >= coords[0]) if f[i][1][0] <= 0 else (f[i][0][0] <= coords[0])) and ((f[i][0][1] >= coords[1]) if f[i][1][1] <= 0 else (f[i][0][1] <= coords[1])) and ((f[x][0][0] >= coords[0]) if f[x][1][0] <= 0 else (f[x][0][0] <= coords[0])) and ((f[x][0][1] >= coords[1]) if f[x][1][1] <= 0 else (f[x][0][1] <= coords[1])):
                    counter += 1
        

print(counter)


#19523