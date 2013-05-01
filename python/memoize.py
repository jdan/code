#!/usr/bin/python
#
# Jordan Scales (http://jordanscales.com)
# 5/1/13
#
# A walkthrough of a simple (but useful!) use of decorators to memoize functions

def memoize(f):
    if not hasattr(f, 'cache'):             # define a `cache` property on our function
        f.cache = {}                        #   if we haven't already

    def inner(*args):                       # inner function gets the args sent by f
        if f.cache.has_key(args):           # if we get a cache hit
            return f.cache[args]            #   return the cached value
        else:
            res = f.cache[args] = f(*args)  # set the cache (and temporary result) to the return value
            return res                      # return the result

    return inner                            # return our inner function

@memoize
def fib(n):                                 # fibonacci's a good example
    if n < 2:                               # fib(n-2) will be counted twice!
        return n                            #    fib(n-1)   => *fib(n-2)* + fib(n-3)
    return fib(n-1) + fib(n-2)              #   *fib(n-2)*  =>  fib(n-3)  - fib(n-4)
                                            #       note: fib(n-3) will be computed *four* times (etc.)

print fib(50)                               # without memoization, fib(50) will take a long, long time
                                            #   python@master -> time python memoize.py
                                            #   12586269025
                                            #   
                                            #   real    0m0.039s
                                            #   user    0m0.026s
                                            #   sys 0m0.011s
                                            #   python@master ->
