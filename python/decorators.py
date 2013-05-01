#!/usr/bin/python
# Decorators example
# Jordan Scales (http://jordanscales.com)
# 5/1/13

# First example, adding 1 to function output
def addone(f):
    def inner():
        return 1 + f()
    return inner

@addone
def six():
    return 6

# Second example, removing some of the arguments
def remove_first_arg(f):
    def inner(*args):
        return f(*args[1:])
    return inner

@remove_first_arg
def sum_args(*args):
    return sum(args)

print six()
print sum_args(5, 6, 7)
