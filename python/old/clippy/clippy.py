from bottle import route, run
import random

clips = {}

@route('/:n')
def re(n):
    code = n.split('=')[1]
    if code not in clips:
        return 'not found'
    else:
        return clips[code]

@route('/post/:n')
def post(n):
    code = str(random.randint(0, 99999)).rjust(5, '0')
    clips[code] = n
    return code

run(host='155.246.116.24', port=8080)
