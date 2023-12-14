f = [[x for x in i.split('\n')] for i in open('input.txt', 'r').read().split('\n\n')]
c = 0

for i in f:
    print()
    print(i)
    row, column = -1, -1
    for x in range(len(i[0])-1):
        for j in range(x + 1, len(i[0])):
            if x == 0 or j == len(i[0]) - 1:
                o = [''.join([i[y][z] for y in range(len(i))]) for z in range(x, j + 1)]
                if o[:len(o)//2] == o[len(o)//2:][::-1]:
                    column = (j + x) // 2 + 1
                    break
        else:
            continue
        break
    else:
        for x in range(len(i)-1):
            for j in range(x + 1, len(i)):
                if x == 0 or j == len(i) - 1:
                    o = i[x:j+1]
                    if o[:len(o)//2] == o[len(o)//2:][::-1]:
                        row = (j + x) // 2 + 1
                        break
            else:
                continue
            break

    ccc = False
    for m in range(len(i)):
        for k in range(len(i[0])):
            i[m] = i[m][:k] + ('.' if i[m][k] == '#' else '#') + i[m][k+1:]
            for x in range(len(i[0])-1):
                for j in range(x + 1, len(i[0])):
                    if (x == 0 or j == len(i[0]) - 1) and not (column != -1 and column == (((x + j) // 2) + 1)):
                        o = [''.join([i[y][z] for y in range(len(i))]) for z in range(x, j + 1)]
                        if o[:len(o)//2] == o[len(o)//2:][::-1]:
                            c += (((x + j) // 2) + 1)
                            print((((x + j) // 2) + 1))
                            ccc = True
                            break
                else:
                    continue
                break
            else:
                for x in range(len(i)-1):
                    for j in range(x + 1, len(i)):
                        if (x == 0 or j == len(i) - 1) and not (row != -1 and row == (((x + j) // 2) + 1)):
                            o = i[x:j+1]
                            if o[:len(o)//2] == o[len(o)//2:][::-1]:
                                c += 100 * (((x + j) // 2) + 1)
                                print(100 * (((x + j) // 2) + 1))
                                ccc = True
                                break
                    else:
                        continue
                    break
            i[m] = i[m][:k] + ('.' if i[m][k] == '#' else '#') + i[m][k+1:]

            if ccc:
                break
        if ccc:
            break



print(c)