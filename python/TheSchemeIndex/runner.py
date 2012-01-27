import os
from time import sleep

def runscript(filename, command, limit = 1):
	reader = open(r'%s/%s.rkt' % (filename, filename))
	
	# create an execute command
	execute = reader.read()
	reader.close()
	
	# add the command
	execute += '(display %s)(newline)' % command
	
	# remove the newline escapes (for good measure)
	execute = ' '.join(execute.split('\n'))
	
	# write "execute" to a temporary racket file
	writer = open('/home/jordan/TheSchemeIndex/%s/%s_tmp.rkt' % (filename, filename), 'w')
	writer.write(execute)
	writer.close()
	
	os.system('bash limit.sh %s/%s_tmp.rkt %s > %s/%soutput' % (filename, filename, limit, filename, filename))
	
	reader = open('%s/%soutput' % (filename, filename))
	ret = reader.read()
	reader.close()
	
	os.system('rm %s/%soutput' % (filename, filename))
	os.system('rm /home/jordan/TheSchemeIndex/%s/%s_tmp.rkt' % (filename, filename))
	return ret
