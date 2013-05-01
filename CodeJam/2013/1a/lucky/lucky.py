#!/usr/bin/python

from sys import argv

def arrangements(n, a, m):
    ''' n numbers between a and m in increasing order '''
    if n == 1:
        return map(lambda i: [i], list(range(a, m+1)))
    else:
        flatten = lambda ls: reduce(lambda a, b: a + b, ls)
        return flatten([map(lambda ls: [i] + ls, arrangements(n - 1, i, m)) for i in range(a, m+1)])

def main():
    f = file(argv[1])
    _ = int(f.readline())

    r, n, m, k = map(int, f.readline()[:-1].split(' '))

    print 'Case #1:'

    for i in range(r):
        nums = map(int, f.readline()[:-1].split(' '))

        # n numbers between 2 and m

        # get the biggest number
        biggest = max(nums)
        # you know this is (probably) a product of all numbers

        found = False

        for arrange in arrangements(n, 2, m):
            if biggest == reduce(lambda a, b: a * b, arrange):
                print ''.join(map(str, arrange))
                found = True
                break

        if not found:
            print '2' * n

if __name__ == '__main__':
    main()

