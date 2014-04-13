cases = int(raw_input())

for i in range(cases):
    row1 = int(raw_input())

    # card# => [row1, row2]
    arrangementMap = {}
    arrangementMapInverse = {}
    badMagician = False

    arrangement1 = []
    for a in range(4):
        row = map(int, raw_input().split(' '))

        for b in row:
            arrangementMap[b] = [a+1]

        arrangement1.append(row)

    row2 = int(raw_input())
    arrangement2 = []
    for a in range(4):
        row = map(int, raw_input().split(' '))

        for b in row:
            arrangementMap[b].append(a+1)
            pair = (arrangementMap[b][0], arrangementMap[b][1])

            if pair == (row1, row2) and pair in arrangementMapInverse:
                badMagician = True

            arrangementMapInverse[pair] = b

        arrangement2.append(row)

    # Did the volunteer cheat?
    if (row1, row2) not in arrangementMapInverse:
        print 'Case #%d: Volunteer cheated!' % (i+1)

    elif not badMagician:
        print 'Case #%d: %d' % (i+1, arrangementMapInverse[(row1, row2)])

    # Is the magician bad?
    else:
        print 'Case #%d: Bad magician!' % (i+1)

    # Otherwise, print the card

