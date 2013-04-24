#!/usr/bin/python

from sys import argv
from math import sqrt

def main():
    f = file(argv[1])
    n = int(f.readline())

    for i in range(n):
        k, nchests = map(int, f.readline()[:-1].split(' '))
        keys = map(int, f.readline()[:-1].split(' '))

        chest_index = list(range(1, nchests+1))
        chests = []
        moves = []

        for q in range(nchests):
            numbers = map(int, f.readline()[:-1].split(' '))
            chests.append((numbers[0], numbers[2:]))

        possible = False
        while len(keys) > 0:
            if chests == []:
                possible = True
                break

            # can we open any chests? 
            # no, impossible
            # yes, open the first possible chest
            #   remove the key
            #   add the keys inside the chest to keys
            #   remove the chest from chests
            #   remove the index from chests_index
            opened_one = False
            best_index = -1
            best_amount = -1
            best_key_index = -1
            for current_index in range(len(chests)):
                key_index = indexOf(keys, chests[current_index][0])

                if key_index > -1:
                    if len(chests[current_index][1]) > best_amount:
                        best_amount = len(chests[current_index][1])
                        best_index = current_index
                        best_key_index = key_index

            if best_index > -1:
                moves.append(chest_index[best_index])

                keys = without(keys, best_key_index)
                keys = keys + chests[best_index][1]

                chests = without(chests, best_index)
                chest_index = without(chest_index, best_index)

                possible = True
            else:
                possible = False
                break

        if possible:
            print 'Case #%s: %s' % (str(i + 1), ' '.join(map(str, moves)))
        else:
            print 'Case #%s: IMPOSSIBLE' % (str(i + 1))

def without(arr, i):
    ''' returns an array, missing index i '''
    return arr[:i] + arr[i+1:]

def indexOf(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1

if __name__ == '__main__':
    main()
