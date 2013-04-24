#!/usr/bin/python

from sys import argv

def main():
    f = file(argv[1])
    n = int(f.readline())

    for i in range(n):
        h, w = map(int, f.readline()[:-1].split(' '))

        lawn = []
        for r in range(h):
            lawn.append(map(int, f.readline()[:-1].split(' ')))

        # so what's impossible?
        # any sort of "pit"
        # so if we have
        #   3 3 3
        #   3 1 3
        #   3 3 3
        # it is invalid
        #
        # so we need to check that any given point can make it to the outside
        # by only crossing points with a lower height than it

        # if has_pits(lawn):
        #     print 'Case #%s: NO' % (i + 1)
        # else:
        #     print 'Case #%s: YES' % (i + 1)

        # strategy
        # go over each row
        # if the lawnmower can go through (there are all ones),
        #   go through and set all ones to 0
        # otherwise, continue
        # then, do the same for each column
        #
        # if there are no ones, we succeeded

        for r in range(h):
            if lawn[r] == [1] * w:
                lawn[r] = [0] * w

        for c in range(w):
            # check if the column is all 1's and 0's
            if all_1s_and_0s(get_column(lawn, c)):
                for t in range(h):
                    lawn[t][c] = 0

        # check for ones
        has_ones = False
        for j in lawn:
            for k in j:
                if k == 1:
                    has_ones = True
                    break
            if has_ones:
                break

        if has_ones:
            print 'Case #%s: NO' % (i + 1)
        else:
            print 'Case #%s: YES' % (i + 1)

def all_1s_and_0s(arr):
    for item in arr:
        if item != 0 and item != 1:
            return False
    return True

def get_column(arr, n):
    ''' returns the nth column in an array '''
    col = []
    for row in arr:
        col.append(row[n])
    return col

def has_pits(arr):
    for r in range(len(arr)):
        if r == 0 or r == len(arr) - 1:
            continue

        for c in range(len(arr[0])):
            if c == 0 or c == len(arr[0]) - 1:
                continue

            # we are somewhere INSIDE of the array
            # if we have to climb up 

def local_mins(arr):
    ''' returns the locations of the local mins in the array '''
    lm = []
    for index, val in enumerate(arr):
        if index == 0:
            continue
        elif index == len(arr) - 1:
            continue
        else:
            # we are somewhere inside the array
            if arr[index-1] > val and arr[index+1] > val:
                lm.append(index)
    return lm

def has_pits(lawn):
    return True

if __name__ == '__main__':
    main()
