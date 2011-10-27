from bottle import route, run
from time import sleep
import os
import random

@route('/')
def index():
    return '''
<html>
<head>
<title>PyRunner 1.0</title>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"></script>
<script type="text/javascript">
function submit_code() {
    var c = escape(document.getElementById("code").value);
    $.get("upload/" + c, function(data) {
        var d = data;

        $.get("getoutput/" + d, function(data) {
            document.getElementById("output").value = data;
        });
    });
}
</script>
</head>

<body>
<h3>enter code and click submit</h3>
<br />

<textarea id="code" rows="22" cols="100" style="font-family: lucida console;"></textarea>
<br />
<input type="button" value="Submit" onclick="submit_code()" />
<br />
<h3>output</h3>
<textarea id="output" rows="22" cols="100" style="font-family: lucida console;"></textarea>
</body>
</html>
'''

@route('/upload/:code')
def upload(code):
    name = str(random.randint(1, 99999999)).rjust(8,'0')
    writer = open('outputs/%s.py' % name, 'w')
    writer.write(code)
    writer.close()

    os.system('python outputs/%s.py > outputs/%s.txt' % (name, name))
    os.system('rm outputs/%s.py' % name)

    return name

@route('/getoutput/:code')
def getoutput(code):
    reader = open('outputs/%s.txt' % code, 'r')
    o = reader.read()
    reader.close()

    os.system('rm outputs/%s.txt' % code)

    return o

run(host='192.168.1.7', port='7777')
