from bottle import route, run
import os

@route('/')
def main():
    return '''<html>
<head><title>imgirror</title></head>
<body>
<h2>imgirror</h2>
<p>To use...</p>
<p>http://96.242.135.162:7777/img/<i>imgur_code</i></p>
<p>For example: <a href="http://96.242.135.162:7777/img/v0wBg">http://96.242.135.162:7777/img/v0wBg</a></p>
<p>(Sorry it's so slow, Shrank)</p>
</body>
</html>'''

@route('/img/:code')
def img(code):
    os.system('wget -O /var/www/img/%s.jpg http://i.imgur.com/%s.jpg' % (code, code))
    return '''<html>
<head><title>%s.jpg</title></head>
<body>
<h2>%s.jpg</h2>
<img src="http://96.242.135.162:8080/img/%s.jpg" />
</body>
</html>''' % (code, code, code)

run(host='192.168.1.4', port='7777')
