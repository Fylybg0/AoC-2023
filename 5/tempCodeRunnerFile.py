
    while current != 'location':
        new = []
        while ranges != []:
            for y in fd[(current, fg[current])]:
                over = overlap(ranges[0], (y[1], y[1] + y[2] - 1))
                if over != None:
                    new.append((over[0][0] - y[1] + y[0], over[0][1] - y[1] + y[0]))
                    ranges += over[1]
                    ranges.pop(0)
                    break
            else: