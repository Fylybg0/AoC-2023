
def isPossible(line, pos, following, line_len, fixed):
    for fix in fixed:
        if pos <= fix[1] <= pos + following:
            print('sss')
            return (pos == 0 or line[pos-1] != '#') and max(fix[1] + fix[0], pos + following) - pos == following
    return (pos == 0 or line[pos-1] != '#') and (line_len == pos + following or line[pos+following] != '#')

aaa = ['?', '#', '#', '#', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '#', '#', '#', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '#', '#', '#', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '#', '#', '#', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '#', '#', '#', '?', '?', '?', '?', '?', '?', '?', '?']
print(isPossible(aaa, 1, 3, len(aaa), [(3, 53), (3, 40), (3, 27), (3, 14), (3, 1)]))
