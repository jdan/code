#!/usr/bin/python

import re

f = file('comments')
contents = f.read()
f.close()

chunks = contents.split('\n\n')
res = []

for chunk in chunks:
  messages = chunk.split('\n')
  messages_new = []
  for message in messages:
    name = ' '.join(message.split()[:2])
    body = ' '.join(message.split()[2:])
    messages_new.append([name, body])
  
  res.append(messages_new)
  
total         = len(res)
replied_to    = sum(map(lambda i: len(i) > 1, res))
first         = res[-1][0][0]
longest       = max(map(lambda i: [len(i[0][1]), i[0][0]], res))
shortest      = min(map(lambda i: [len(i[0][1]) if len(i[0][1]) > 0 else 1000, i[0][0]], res))
longest_convo = max(map(lambda i: [len(i) if len(i) < 10 else -1000, i[0][0]], res))
most_excited  = max(map(lambda i: [len(re.findall('!', i[0][1])), i[0][0]], res))
most_caps     = max(map(lambda i: [len(re.findall(r"[A-Z]", i[0][1])), i[0][0]], res))
most_punc     = max(map(lambda i: [len(re.findall(r"\.|\,|\!|\?", i[0][1])), i[0][0]], res))

print 'Results'
print 'Total:\t\t\t%s' % total
print 'Replied to:\t\t%s (%s%%)' % (replied_to, str(float(100 * replied_to) / total)[:5])
print 'First:\t\t\t%s' % first
print 'Longest:\t\t%s (%s chars)' % (longest[1], longest[0])
print 'Shortest:\t\t%s (%s chars)' % (shortest[1], shortest[0])
print 'Longest Conversation:\t%s (%s replies)' % (longest_convo[1], longest_convo[0])
print 'Most Excited (!!):\t%s (%s x \'!\')' % (most_excited[1], most_excited[0])
print 'MOST CAPS:\t\t%s (%s)' % (most_caps[1], most_caps[0])
print 'Most. Punctunation.:\t%s, (%s).' % (most_punc[1], most_punc[0])