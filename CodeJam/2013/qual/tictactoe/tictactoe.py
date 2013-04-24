#!/usr/bin/python

from sys import argv

def main():
    f = file(argv[1])
    n = int(f.readline())

    for i in range(n):
        board = []
        for r in range(4):
            board.append(list(f.readline()[:-1]))

        Xboard = replace_board(board, 'T', 'X')
        Oboard = replace_board(board, 'T', 'O')

        if check_rows(Xboard, 'X') or check_cols(Xboard, 'X') or check_diags(Xboard, 'X'):
            print 'Case #%s: X won' % (i + 1)
        elif check_rows(Oboard, 'O') or check_cols(Oboard, 'O') or check_diags(Oboard, 'O'):
            print 'Case #%s: O won' % (i + 1)
        elif is_full(board):
            print 'Case #%s: Draw' % (i + 1)
        else:
            print 'Case #%s: Game has not completed' % (i + 1)

        f.readline()

def replace_board(board, target, replacement):
    new_board = []
    for r in range(4):
        row = []
        for c in range(4):
            if board[r][c] == target:
                row.append(replacement)
            else:
                row.append(board[r][c])

        new_board.append(row)
    return new_board

def check_rows(board, player):
    for r in range(4):
        if board[r] == [player] * 4:
            return True
    return False

def check_cols(board, player):
    for c in range(4):
        if [board[0][c], board[1][c], board[2][c], board[3][c]] == [player] * 4:
            return True
    return False

def check_diags(board, player):
    if [board[0][0], board[1][1], board[2][2], board[3][3]] == [player] * 4:
        return True

    if [board[3][0], board[2][1], board[1][2], board[0][3]] == [player] * 4:
        return True

def is_full(board):
    for r in range(4):
        for c in range(4):
            if board[r][c] == '.':
                return False
    return True

if __name__ == '__main__':
    main()
