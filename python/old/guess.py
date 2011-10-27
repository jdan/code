import random

max_bound = 10000000
trials = 1000

def evaluate(a, b): 
	if a > b:
		return 'Too high!'
	elif a < b:
		return 'Too low!'
	else:
		return 'Correct!'

print 'Max Bound: %s' % max_bound
print ''

print 'Binary Search'
print ''
total_guesses = 0
for i in range(trials):
	guesses = 0
	incr = 0
	guess = max_bound / 2
	real_num = random.randint(1, max_bound)
	while guess <> real_num:
		incr += 1
		guesses += 1
		print 'Guess: %s' % guess
		print evaluate(guess, real_num)
		print '--------------------'

		if (max_bound / (2 ** (incr + 1))) == 0:
			d = 1
		else:
			d = (max_bound / (2 ** (incr + 1)))
		
		if evaluate(guess, real_num) == 'Too high!':
			guess -= d
		else:
			guess += d
			
	print 'Guess: %s' % guess
	print evaluate(guess, real_num)
	print '--------------------'
	print 'It took %s guesses' % (guesses)
	print ''
	total_guesses += guesses
	
print 'Average: %s guesses' % (float(total_guesses) / trials)
