#!/usr/bin/python

f = file('B-large.in')
n = int(f.readline())

for i in range(n):
    line = f.readline().split()
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    scores = map(int, line[3:])
    
    # 1st score is best
    # 2nd and 3rd are 1 less
    # k + (k - 1) + (k - 1)
    # 3k - 2, k is the best score
    
    # does 3k - 1 = S have a solution?
    #    is k >= p?
    #        if not, check 3k - 4 (counts as surprising)
    # does 3k - 2 = S have a solution?
    # if so, is k >= p ?
    # does 3k - 3 have a solution? 
    #    if so, (counts as surprising)
    
    res = 0
    
    for score in scores:
        if score % 3 == 0:
            k = score / 3
            if k >= p:
                res += 1
            elif S > 0 and score >= 3:
                k = (score + 3) / 3
                if k >= p:
                    res += 1
                    S -= 1
        elif (score + 1) % 3 == 0:
            k = (score + 1) / 3
            if k >= p:
                res += 1
            elif S > 0 and score >= 2:
                k = (score + 4) / 3
                if k >= p:
                    res += 1
                    S -= 1
        elif (score + 2) % 3 == 0:
            k = (score + 2) / 3
            if k >= p:
                res += 1
               
    print 'Case #%s: %s' % (i+1, res)