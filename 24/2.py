from sympy import solve, symbols

f = [[[int(z) for z in x.split(', ')] for x in i.split(' @ ')] for i in open('input.txt', 'r').read().strip().split('\n')]
mn, mx = 200000000000000, 400000000000000


lx = symbols('lx')
ly = symbols('ly')
lz = symbols('lz')
dx = symbols('dx')
dy = symbols('dy')
dz = symbols('dz')

lx1, ly1, lz1 = f[0][0]
lx2, ly2, lz2 = f[1][0]
lx3, ly3, lz3 = f[2][0]
dx1, dy1, dz1 = f[0][1]
dx2, dy2, dz2 = f[1][1]
dx3, dy3, dz3 = f[2][1]

#lx + dx * t = 0
#lx + dx * t = 0
#lx + dx * t = 0
#(lx1 - lx) + (dx1 - dx) * (-lx/dx)
#(ly1 - ly) + (dy1 - dy) * (-ly/dy)
#(lz1 - lz) + (dz1 - dz) * (-lz/dz)

solutions = solve( [(lx-lx1)*(dy-dy1)-(ly-ly1)*(dx-dx1), (ly-ly1)*(dz-dz1)-(lz-lz1)*(dy-dy1), 
                    (lx-lx2)*(dy-dy2)-(ly-ly2)*(dx-dx2), (ly-ly2)*(dz-dz2)-(lz-lz2)*(dy-dy2), 
                    (lx-lx3)*(dy-dy3)-(ly-ly3)*(dx-dx3), (ly-ly3)*(dz-dz3)-(lz-lz3)*(dy-dy3) ], [lx, ly, lz, dx, dy, dz], dict=True)

for solution in solutions:
    if solution[lx] % 1 == 0 and solution[ly] % 1 == 0 and solution[lz] % 1 == 0:
        print(solution[lx] + solution[ly] + solution[lz])
        break