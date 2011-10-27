# polyguess.py
# Jordan Scales
# 3/17/2011
#
# Chooses a random polynomial (with a random degree), and gives some digits
# The player must guess the next number in the series

import random

right = 0
wrong = 0

while 1:
    difficulty = 4
    while difficulty > 3 or difficulty < 1:
        difficulty = int(raw_input('Enter a difficulty (1-3): '))
        
    degree = random.randint(difficulty, difficulty + 1)
    coefficients = []

    for i in range(degree):
        coefficients.append(random.randint(0, 5 - difficulty))

    starting_point = random.randint(1, 5*difficulty)
    number_of_terms = random.randint(degree + 1, degree + (4 - difficulty))

    def poly(x, coefs):
        t = 0
        for i in range(len(coefs)):
            t += coefs[i] * (x ** (len(coefs) - i - 1))
            
        return t

    wanted = poly(starting_point + number_of_terms, coefficients)
    
    s = ''
    for a in range(number_of_terms):
        s += str(poly(starting_point + a, coefficients)) + ' '

    print 'Difficulty: %s' % difficulty
    print s
    response = int(raw_input('What is the next number in the series? '))

    if response == wanted:
        print 'Correct!'
        right += 1
    else:
        print 'Wrong, correct answer was %s' % wanted
        wrong += 1

    print 'Right: %s\nWrong: %s' % (right, wrong)


