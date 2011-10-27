import twitter

api = twitter.Api(username='AverageBot', password='avg01234')

def avg(l):
	t = 0
	for entry in l:
		try:
			t += int(entry)
		except:
			print 'Whoops!'
			
	return float(t) / len(l)

i = api.GetReplies()[0]
user_from = i.user.screen_name
t = i.text.split(' ')[1:]

result = 0

if t[0] == 'average' or t[0] == 'avg':
	result = avg(t[1:])
elif t[0] == help:
	result = 'Message "average" followed by some numbers separated by spaces.'
	
api.PostUpdate('@%s : %s' % (user_from, result))
