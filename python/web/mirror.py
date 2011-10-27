from bottle import route, run
from urllib import urlopen

@route('/mirror/:url')
def mirror(url):
    try:
        if url.endswith('.com'):
            url = url[:-4]
        return urlopen('http://' + url + '.com').read()
    except Exception:
        return 'Don\'t include the "http://"!'

@route('/')
def index():
    return '<h1>It works!</h1>'

run(host='192.168.1.2', port=7777)
