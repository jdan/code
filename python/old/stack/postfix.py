from stack import *

inp = raw_input('? ')
digits = inp.split(' ')

opers = {'+' : (lambda a, b: b + a),
         '-' : (lambda a, b: b - a),
         '*' : (lambda a, b: b * a),
         '/' : (lambda a, b: b / a),
         '^' : (lambda a, b: b **a)}

s = Stack(len(digits))
for i in digits:
    if i in opers:
        s.push(opers[i](s.pop(), s.pop()))
    else:
        s.push(int(i))

print s.top()
