cases = int(raw_input())

def withNFarms(C, F, X, n):
    totalTime = 0

    for i in range(n):
        totalTime += C / (2 + F*i)

    return totalTime + X / (2 + F*n)

memo = {}
def withNFarmsFast(C, F, X, n):
    if (C, F, X, n) in memo:
        return memo[(C, F, X, n)]

    # base case
    if n == 0:
        memo[(C, F, X, n)] = X / 2
        return X / 2
    else:
        recursive = withNFarmsFast(C, F, X, n-1)

        # substract the last X / (2 + (n-1)*F)
        # replace that X with C
        # add X / (2 + n*F)

        result = recursive - X / (2 + (n-1)*F) \
                           + C / (2 + (n-1)*F) \
                           + X / (2 + n*F)

        memo[(C, F, X, n)] = result
        return result

for i in range(cases):
    C, F, X = map(float, raw_input().split(' '))

    # base time, without buying any farms
    time = withNFarms(C, F, X, 0)
    n = 1

    while True:
        if withNFarmsFast(C, F, X, n) < time:
            time = withNFarmsFast(C, F, X, n)
            n += 1
        else:
            break

    print 'Case #%d: %.7f' % (i+1, time)
