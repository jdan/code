def main():
    output = ''

    f = file('in.chess')
    contents = f.readlines()
    f.close()

    turn = 0
    board = [['r','n','b','q','k','b','n','r'],
             ['p','p','p','p','p','p','p','p'],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' ',' ',' '],
             ['P','P','P','P','P','P','P','P'],
             ['R','N','B','Q','K','B','N','R']]

    for line in contents:
        s = line.split()
        mfrom = s[3]
        mto = s[5]

        fromx = int(mfrom[1]) - 1
        fromy = 'ABCDEFGH'.index(mfrom[0])

        tox = int(mto[1]) - 1
        toy = 'ABCDEFGH'.index(mto[0])

        piece = board[fromx][fromy]

        taken = ''
        if board[tox][toy] != ' ':
            taken = 'x'

        board[fromx][fromy] = ' '
        board[tox][toy] = piece

        if piece == 'p' or piece == 'P':
            piece = ''
        piece = piece.upper()

        nota = piece + mfrom[0].lower() + taken + 'abcdefgh'[toy] + str(tox + 1)

        if turn % 2 == 0:
            output += '%s. %s ' % (turn / 2 + 1, nota)
        else:
            output += '%s ' % (nota)

        turn += 1

    print output

if __name__ == '__main__':
    main()
