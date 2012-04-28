#!/usr/bin/python
# Jordan Scales - http://jordanscales.com - http://github.com/prezjordan
# CodeJam 2012 Round 1A

from sys import argv

def main():
    f = open(argv[1])
    n = int(f.readline())

    for i in range(n):
        levels = int(f.readline())
        reqs = []
        for k in range(levels):
            reqs.append(map(int, f.readline().split()))
        
        # strategy - GREEDY
        # while availability matrix is not all zeros
        # check each game's 2-star requirement (from the bottom)
        #   complete as many as you can
        # check each game's 1-star requirement
        
        stars = 0
        games_played = 0
        
        while True:
            found_one = False
            
            # check all level-2s
            for c, req in enumerate(reqs):
                if (req[1] != -1) and (stars >= req[1]):
                    games_played += 1
                    found_one = True
                    
                    if req[0] == -1:
                        stars += 1
                    else:
                        stars += 2
                        
                    reqs[c][1] = -1
                    break
                        
            if found_one: continue
            
            # check all level-1s if we haven't done level-2 yet
            for c, req in enumerate(reqs):
                if (req[1] != -1) and (req[0] != -1) and (stars >= req[0]):
                    games_played += 1
                    found_one = True
                    
                    stars += 1
                    reqs[c][0] = -1
                    break
                        
            if not found_one:
                break
                
        all_done = True
        for req in reqs:
            if req[1] > -1:
                all_done = False
                break
        
        if all_done:
            print 'Case #%s: %s' % (i + 1, games_played)
        else:
            print 'Case #%s: Too Bad' % (i + 1)

if __name__ == '__main__':
    main()