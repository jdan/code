#!/usr/bin/python

s1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
s2 = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

m = {}

for i, c in enumerate(s1):
    if c != ' ':
        m[c] = s2[i]
        
m['q'] = 'z'
m['z'] = 'q'

def translate(s):
    ret = ''
    for c in s:
        if c == ' ':
            ret += ' '
        elif c == '\n':
            pass
        else:
            ret += m[c]
    return ret
        
if __name__ == '__main__':
    f = file('A-small-attempt0.in')
    n = int(f.readline())
    
    for i in range(n):
        word = f.readline()
        print 'Case #%s: %s' % (str(i + 1), translate(word))
        