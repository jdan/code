import string

def strip_ws(s):
    ret = ''
    for char in s:
        if char not in string.whitespace:
            ret += char
    return ret

user_input = raw_input('? ')

brackets = user_input[0] + user_input[-1]
if brackets <> '[]' and brackets <> '{}':
    raise Exception("Invalid format: Please surround your set with brackets")

myset = user_input[1:-1]
output = myset.split('|')[0]
tail = myset.split('|')[1]

output_code = 'ret = []\n' # code we will parse later
tabs = 0

sections = tail.split(',')

# strip whitespace in each item of sections
for i in range(len(sections)):
    sections[i] = strip_ws(sections[i])

loops = []
conds = []

for item in sections:
    if item.find('<-') == -1: # this is a condition
        conds.append(item)
    else:
        var = item.split('<-')[0]
        ran = (','.join(item.split('<-')[1][1:-1].split('.'))).split(',')[::2]

        loops.append([var, ran])

for item in loops:
    output_code += '%sfor %s in range(%s, %s):\n' % ('  ' * tabs, item[0], item[1][0], int(item[1][1]) + 1)
    tabs += 1

for item in conds:
    output_code += '%sif %s:\n' % ('  ' * tabs, item)
    tabs += 1

output_code += '%sret.append(%s)\n' % ('  ' * tabs, strip_ws(output))
output_code += 'print ret'

exec(output_code)
