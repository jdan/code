w = raw_input('Enter a word: ')
r = file('dictionary.txt')
found = False
while not found:
    h = r.readline()[:-1]
    if h == w:
        print 'Found it!'
        found = True
    
