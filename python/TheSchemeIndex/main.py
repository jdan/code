import os
import random
from runner import runscript
from sendmail import sendmail

from bottle import route, run, redirect


@route('/')
def main():
	reader = open('index')
	scripts = []
	
	for line in reader.readlines():
		scripts.append(line.split('@'))  # TITLE, FILENAME, DESCRIPTION, AUTHOR
		
	reader.close()
		
	# output
	output = '<html><head><title>((The Scheme Index))</title></head>\n'
	output += '<body style="margin: 50px; font-family: sans">\n\n'
	output += '<h1>((The Scheme Index))</h1>\n'
	output += '<p><a href="submit_form">Submit your own</a></p><br />\n\n'
	
	for script in scripts:
		title = script[0]
		filename = script[1]
		desc = script[2]
		author = script[3]
	
		output += '<div id="%s" style="border: 2px solid #000; padding-left: 15px; margin-bottom: 20px;">\n' % filename
		output += '<h3>%s</h3>\n' % title
		output += '<p><i>%s</i></p>\n' % desc
		output += '<p>By: %s</p>\n' % author
		output += '<p><a href="view/%s">Click here to view %s</a></p>\n' % (filename, filename)
		output += '</div>\n\n'
		
	output += '</body></html>'
	
	return output
	
@route('/view/:script')
def view(script):
	try:
		reader = open('%s/%s.rkt' % (script, script))
		src = reader.read()
		reader.close()
		
		# get the data entry for this script
		data = []
		
		reader = open('index')
		for line in reader.readlines():
			if line.startswith(script):
				data = line.split('@')
				
		title = data[0]
		filename = data[1]
		desc = data[2]
		author = data[3]
		
		output = '<html><head>\n'
		output += '<title>%s</title>\n' % title
		
		output += '<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script>\n'
		output += '<script type="text/javascript">'
		
		output += '''
		
		function runcode() {
			$.get('../run/%s/' + escape($("#query").val()), function(data) {
				$("#result").html(data);
			});
		}
		
		''' % filename
		
		output += '</script>'
		
		output += '</head>\n'
		output += '<body style="margin: 50px; font-family: sans">\n\n'
		output += '<h1>%s.rkt</h1>\n' % filename
		output += '<i>by %s</i><br /><br />\n' % author
		
		output += 'Description: <br />\n'
		output += '<div id="desc" style="border: 2px solid #000; padding: 10px;">\n'
		output += '%s\n' % desc
		output += '</div><br />\n\n'
		
		output += 'Source Code: <br />\n'
		output += '<div id="src" style="border: 2px solid #000; padding-left: 10px;">\n'
		output += '<pre>\n'
		output += src + '\n'
		output += '</pre>\n'
		output += '</div><br />\n'
		
		output += 'Run Query: <br />\n'
		output += '<input type="text" id="query" style="width: 300px;" /><br />\n'
		output += '<input type="button" value="Submit" onclick="runcode()" />\n'
		output += '<br /><br />\n'
		
		output += 'Result: <br />\n'
		output += '<div id="result" style="border: 1px solid #666; padding: 10px; color: #33a;">&nbsp</div>\n'
		output += '<br /><br />\n'
		
		output += '<a href="../">Return to Index</a>\n'
		output += '</body></html>'
		
		return output
		
	except IOError:
		return 'Sorry, file not found.'
		
@route('/run/:filename/:command')
def runcode(filename, command):
	return runscript(filename, command)

@route('/submit_form')
def submit_form():
	output = '''
<html>
<head>
	<title>Submit Code</title>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script>
<script type="text/javascript">
function sendinfo() {
	$.get('../submit/' + escape($("#name").val()) + '/' + remove_slash(escape($("#desc").val())) + '/' + remove_slash(escape($("#source").val())) + '/' + escape($("#pipeline").val()), function(data) {
		if (data == "ERR") {
			$("#result").html("<b>OOPS: </b>Something went wrong.");
			$("#result").css("background-color: #c34");
		} else {
			$("#result").html("<b>NOTE: </b>An email has been sent to your pipeline address for confirmation.");
			$("#result").css("background-color: #3c4");
		}
	});
}

function remove_slash(fix) {
    fix = fix.replace("/", "_SLASH")
    if (fix.indexOf("/") != -1) {
       remove_slash(fix);
    } else {
       return fix;
    }
}
</script>
</head>
<body style="margin: 50px; font-family: sans">
<h1>((Submit Code))</h1>

<p>(name): [example: max(mylist)]</p>
<input type="text" id="name" style="width: 600px;" />
<p>(description): [example: finds the max value of a list]</p>
<input type="text" id="desc" style="width: 600px;" />
<p>(source code):</p>
<textarea id="source" rows="15" style="width: 600px;"></textarea>
<p>(pipeline id):</p>
<input type="text" id="pipeline" style="width: 600px;" />
<br />
<input type="button" value="Submit" onclick="sendinfo()" />
<br />
<div id="result"></div>
</body>
</html>
'''
	return output
	
@route('/submit/:name/:desc/:source/:pipeline')
def submit(name, desc, source, pipeline):
	file_name = name.split('(')[0]
	if len(file_name) > 0 and len(desc) > 0 and len(desc) < 100 and len(source) > 0 and len(source) < 2000:
		file_name = file_name.split(' ')[0]
		source = source.replace('_SLASH', '/')
		
		if pipeline.find('@') > 0:
			pipeline = pipeline.split('@')[0]
			
		# make a folder, and write the source
		os.system('mkdir %s' % file_name)
		writer = open(r'%s/%s.rkt' % (file_name, file_name), 'w')
		writer.write(source)
		writer.close()
		
		## DON'T LET THEM OVERWRITE
		if os.path.exists('%s'):
			return 'Sorry, that\'s already been taken.'
		
		# add to the queue
		writer = open('queue','a')
		
		# generate a code
		code = ''
		for i in range(10):
			code += str(random.randint(0, 9))
		
		writer.write(name + '@')
		writer.write(file_name + '@')
		writer.write(desc + '@')
		writer.write(pipeline + '@')
		writer.write(code+'\n')
		writer.close()
		
		# email them
		body = '''
Hi %s,
		 			  
To confirm your recent submission of "%s", please click the link below.
		 			  
http://96.242.135.162:7777/confirm/%s
		 			  
Thanks,
((TheSchemeIndex))''' % (pipeline, name, code)
		 		
		sendmail('%s@stevens.edu' % pipeline, 
		 		 'Confirm your submission of "%s"' % name, 
		 		 body)
		
		print 'email sent'
		return 'email sent'
	else:
		return 'ERR'
		
@route('/confirm/:code')
def confirm(code):
	reader = open('/home/jordan/TheSchemeIndex/queue')
	q = []
	for line in reader.readlines():
		q.append(line.split('\n')[0].split('@'))
	reader.close()
	
	save_name = ''
	# look for the code in each
	for item in q:
		if item[4] == code:
			# add it to the index
			writer = open('index', 'a')
			writer.write('@'.join(item[:4]) + '\n')
			writer.close()
			
			# save its name
			save_name = item[1]

			# remove it from the queue
			q.remove(item)
			break
	
	# rewrite the queue
	writer = open('queue', 'w')
	for item in q:
		writer.write('@'.join(item) + '\n')
		
	writer.close()
	
	redirect('../view/%s' % save_name)
	
run(host='192.168.1.8', port='7777')
