cases = int(raw_input())

for i in cases:
    r, c, mines = map(int, raw_input().split(' '))

    if r < 3 and c < 3:
        print 'Case #%d:' % (i + 1)
        print 'Impossible'
        continue


