import random
import math

matches = 0
trials = 50000000

for i in range(0,trials):
    x = random.random() * 1.5
    y = random.random() * (math.e ** (1.5 ** 2))
    if y < math.e ** (x ** 2):
        matches += 1

print "Trials: %s" % trials
print "Matches: %s" % matches
print "Area: %s" % ((float(matches) / trials) * (1.5 * (math.e ** (1.5 ** 2))))
