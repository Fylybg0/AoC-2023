for i in range(len(f)):
        print(''.join(['O' if (x, i) in rounded_rocks else '#' if (x, i) in cubed_rocks else '.' for x in range(len(f[0]))]))
    print()