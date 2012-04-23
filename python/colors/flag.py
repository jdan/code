#!/usr/bin/python

from colors import RED_BG, BLUE_BG, GRAY_BG, END
width = 70

if __name__ == '__main__':
    print
    
    for row in range(13):
        r = BLUE_BG
        if row == 0 or row == 6:
            r += ' ' * 25
        elif row < 5:
            r += '  ' + '* . ' * 5 + '*  '
        elif row == 5:
            r += '  ' + '*   ' * 5 + '*  '
            
        if row % 2:
            r += GRAY_BG
        else:
            r += RED_BG
    
        r += ' ' * (width - len(r)) + END
        print r
        
    print