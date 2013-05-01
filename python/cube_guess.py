from random import randint

while True:
    n = randint(11, 99)
    print n**3

    guess = int(raw_input('Your guess: '))

    if n == guess:
        print 'Correct!'
    else:
        print 'Oops! The answer was %s' % n

    print
