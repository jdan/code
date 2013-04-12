from bottle import route, run, redirect
import hashlib
import random

class Player:
    def __init__(self, name, password):
        self.name = name
        self.password = password

        m = hashlib.md5()
        m.update(self.password)
        self.id = m.hexdigest()[:8]

class Game:
    def __init__(self, title, password, player):
        self.title = title
        self.password = password
        
        m = hashlib.md5()
        m.update(self.password)
        self.id = m.hexdigest()[:8]
        self.players = []
        self.players.append(player)
        self.moves = []
        self.chat = []
        self.turn = random.randint(0, 1)
        self.score = [0, 0]
        
        self.chat.append([admin.name, 'We\'re waiting on one more player!'])
    
    def add_player(self, player):
        self.players.append(player)
        if len(self.players) == 2:
            self.add_chat(admin, 'Okay, we\'ve got two players. Let\'s get started!')
            self.make_move(admin, self.get_random_two_letter_word())

    def add_chat(self, player, text):
        self.chat.append([player.name, text])
        
    def make_move(self, player, word):   # assuming a valid move has been made
        if len(self.moves) > 0 and self.moves[-1][1] == 'wf':
            if word == 'wf':
                # start a new game
                self.add_chat(admin, 'This game has resulted in a tie!')
                self.add_chat(admin, 'The score is now %s: %s points, %s: %s points' % (self.players[0].name, self.score[0], self.players[1].name, self.score[1]))
                self.reset()
            else:
                self.score[self.turn] += 1
                self.add_chat(admin, '%s wins the round! with "%s"' % (player.name, word))
                self.add_chat(admin, 'The score is now %s: %s points, %s: %s points' % (self.players[0].name, self.score[0], self.players[1].name, self.score[1]))
                self.reset()
        
            return

        self.moves.append([player.name, word])
        if len(self.players) == 2:
            if self.turn == 0:
                 self.turn = 1
            else:
                 self.turn = 0
            self.add_chat(admin, 'It\'s %s\'s turn to play.' % self.players[self.turn].name)

    def get_players(self):
        if len(self.players) == 1:
            return self.players[0].name
        else:
            return self.players[0].name + ', ' + self.players[1].name

    def get_random_two_letter_word(self):
        i = random.randint(0, 102)
        r = open(r'dict/two_letter.txt')
        c = 0
        a = ''
        for line in r:
            c += 1
            if c == i:
                a = line
                break
        r.close()
        return a[:-1]

    def reset(self):
        self.add_chat(admin, 'Starting a new game.')
        self.moves = []
        self.turn = random.randint(0, 1)
        self.make_move(admin, self.get_random_two_letter_word())

admin = Player('Administrator', 'test')
games = []

@route('/')
def main():
    output = '<html><head><title>Wippen Index</title></head><body>'
    output += '<h1>Wippen Index</h1>'
    output += '<div style="margin: 10px; float: right"><a href="/register">Create a New Room</a></div>'
    output += '<table cellspacing="3">'
    output += '<tr><th width="25%" style="text-align: left">Room</th><th width="25%" style="text-align: left">Players</th><th width="25%" style="text-align: left">Last Move</th></tr>'
    
    for game in games:
        output += '<tr><td><a href="/game/%s">%s</a></td><td>%s</td>' % (game.id, game.title, game.get_players())
        if len(game.moves) > 0:
            if game.moves[-1][1] == 'wf':
                output += '<td>%s passed</td></tr>' % game.moves[-1][0]
            else:
                output += '<td>"%s" by %s</td></tr>' % (game.moves[-1][1] , game.moves[-1][0])
        else:
            output += '<td>Waiting...</td></tr>'
    output += '</table>'
    output += '<br /><br /><br /><a href="/whatis">Need Help?</a>'    

    output += '</body></html>'
    return output

@route('/game/:code')
def game(code):
    # find what game it is
    for gam in games:
        g = gam
        if g.id == code[:8]:
            break
    if g.id <> code[:8]:
        return 'Sorry, game not found.<br /><br /><a href="../../">Return</a>'
    output = '<html><head><title>' + g.title + '</title>'
    output += '<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script>'
    output += '''<script type="text/javascript">   
    function submit_chat(text, game_id, your_id) {
        $.get('../../chat/'+game_id+your_id+'/'+escape(text));
        $("#chatinp").val('');
        update_chat(game_id);
    }

    function submit_answer(answer, game_id, your_id) {
        $.get('../../submit/'+game_id+your_id+'/'+escape(answer), function(data){
            if (data != "good") {
                $("#submit_result").html(data);
            } else {
                $("#inp").val('');
                update_gamefield(game_id);
                $("#submit_result").html('');
            }
        });
    }

    function update_gamefield(game_id) {
        $.get('../../get_moves/' + game_id, function(data) {
            $("#gamefield").html(data);
        });
        var gf = document.getElementById('gamefield');
        if (gf.scrollHeight > 406) gf.scrollTop = gf.scrollHeight;
    }

    function update_chat(game_id) {
        $.get('../../get_chat/' + game_id, function(data) {
            $("#chat").html(data);
        });
        var c = document.getElementById('chat');
        if (c.scrollHeight > 406) c.scrollTop = c.scrollHeight;
    }

    var myid = '%s';
    
    setInterval("update_chat(myid)", 2000);
    setInterval("update_gamefield(myid)", 2000);
    </script>''' % g.id
    output+= '</head><body>'
    output += '<h1>' + g.title + '</h1>'
    output += '<p><i>Between %s and %s</p>' % (g.players[0].name, g.players[1].name+'</i>.' if len(g.players) == 2 else 'himself. </i><a href="../../join_game_form/'+g.id+'">JOIN</a>')
    if len(code) == 8:
        output += 'Is this your game? Enter your password: <input type="password" name="code" id="code" />'
        output += '<input type="button" value="Login" onClick="window.location=\'../../goto/' + g.id + '/\' + document.getElementById(\'code\').value" /><br />'

    show_inputs = False
    if len(code) == 16 and (code[8:] == g.players[0].id or (len(g.players) == 2 and code[8:] == g.players[1].id)):
        show_inputs = True

    output += '<div id="leftside" style="width: 55%; float: left">'
    output += '<div id="gamefield" style="border: 1px solid #000; height: 400px; width: 100%; overflow: auto; padding-bottom: 5px"></div>'
    if show_inputs and len(g.players) == 2:
        output += '<input type="text" size="50" id="inp" />'
        output += '<input type="button" value="Submit" onclick="submit_answer(document.getElementById(\'inp\').value, \'%s\', \'%s\')" />' % (code[:8], code[8:])
        output += '<span id="submit_result" style="color: red"></span><br />Type <span style="font-family: lucida console; font-size: 80%">wf</span> to pass!'
    
    output += '<br /><br /><a href="../../">Return to Index</a>' 
    output += '</div>'

    output += '<div id="rightside" style="width: 40%; float: right; margin-right: 30px;">'
    output += '<div id="chat" style="border: 1px solid #000; height: 400px; width: 100%; padding: 3px; overflow: auto"></div>'
    if show_inputs:
        output += '<input type="text" size="35" id="chatinp" /><input type="button" value="Send" onclick="submit_chat(document.getElementById(\'chatinp\').value, \'%s\', \'%s\')" />' % (code[:8], code[8:])
    output += '</div>'    

    output += '</body></html>'
    return output

@route('/create_game/:game_name/:game_pass/:user_name/:user_pass')
def create_game(game_name, game_pass, user_name, user_pass):
    p = Player(user_name, user_pass)
    g = Game(game_name, game_pass, p)
    games.append(g)
    redirect('/game/' + games[-1].id + games[-1].players[0].id)

@route('/join_game_form/:code')
def join_game_form(code):
    output = '<html><head><title>Join Game</title></head><body>'
    output += '<table cellspacing="20"><tr><td colspan="2"><b>Game Info:</b></td></tr>'
    output += '<tr><td>Game Password: </td><td><input type="password" size=20" id="game_password" /></td></tr>'
    output += '<tr><td colspan="2">&nbsp;</td></tr>'
    output += '<tr><td colspan="2"><b>User Info</b></td></tr>'
    output += '<tr><td>Username: </td><td><input type="text" size="20" id="user_name" /></td></tr>'
    output += '<tr><td>Password: </td><td><input type="password" size="20" id="password" /></td></tr>'
    output += '<tr><td colspan="2"><input type="button" value="Submit" onclick="window.location=\'../join_game/%s/\'+' % code
    output += 'escape(document.getElementById(\'game_password\').value) + \'/\' + escape(document.getElementById(\'user_name\').value) +'
    output += '\'/\' + escape(document.getElementById(\'password\').value)" /></td></tr></table></body></html>'
    return output

@route('/join_game/:game_id/:game_pass/:user_name/:user_pass')
def join_game(game_id, game_pass, user_name, user_pass):
    for gam in games:
        g = gam
        if g.id == game_id:
            break
    if g.id <> game_id:
        redirect('/')
    if len(g.players) == 2:
        return 'Sorry, this game is at capacity :(<br /><br /><a href="../../../../game/%s">Go back</a>' % game_id
    if game_pass <> g.password:
        return 'Wrong password :(<br /><br /><a href="../../../../game/%s">Go back</a>' % game_id
    else:
        g.add_player(Player(user_name, user_pass))
        redirect('/goto/%s/%s' % (game_id, user_pass))

@route('/get_chat/:code')
def get_chat(code):
    for gam in games:
        g = gam
        if g.id == code:
            break
    if g.id <> code:
        redirect('/game/' + code)
    output = ''
    for c in g.chat:
        col = ['black', 'blue'][c[0] == 'Administrator']
        output += ('<span style="color:%s">' % col) + c[0] + ': ' + c[1] + '</span><br />'    
    output += '<br />'

    return output
        
@route('/get_moves/:code')
def get_moves(code):
    for gam in games:
        g = gam
        if g.id == code:
            break

    if g.id <> code:
        redirect('/game/' + code)

    output = '<table cellspacing="3">'
    for move in g.moves: 
        output += '<tr style="color: %s"><td style="width: 200px">%s played...</td><td><pre>%s</pre></td></tr>' % ('red' if move[0] == g.players[0].name else 'blue', move[0], 'PASSED' if move[1] == 'wf' else move[1])
    output += '</table><br />'
    return output

@route('/submit/:code/:text')
def submit(code, text):
    game_id = code[:8]
    player_id = code[8:]
    for game in games:
        g = game
        if g.id == game_id:
            break
    if g.id <> game_id:
        return 'Invalid Game ID'
    for player in g.players:
        p = player
        if p.id == player_id:
            break
    if p.id <> player_id:
        return 'Invalid Player ID'
    
    # by this time, the game ID and player ID are valid, now let's check the move
    last_move = g.moves[-1][1]
    if last_move == 'wf':
        last_move = g.moves[-2][1]

    # DIRTY CHEATER
    if text.find('$') > -1 and text.split('$')[1] == 'mad?':
        text = text.split('$')[0]
        g.make_move(p, text)
        return good

    if len(g.players) == 1 or p.id <> g.players[g.turn].id:
        return 'Sorry, you cannot make a move at this time.'
    # make it lower case
    print last_move
    text = text.lower()

    # player wants to pass.
    if text == 'wf':
        g.add_chat(admin, '%s passed!' % p.name)
        g.make_move(p, text)
        return 'good'

    print text
    if len(last_move) < 7 and len(text) <> len(last_move) + 1:
        return 'Sorry, you must add 1 and only one character.'
    if len(last_move) >= 7 and not (len(text) == len(last_move) + 1 or len(text) == len(last_move)):
        return 'Sorry, you must either substitute a letter or add one.'
    if text == last_move + 's':
        return 'Sorry, you cannot make the word plural.'
    
    current_move_chars = list(text)
    last_move_chars = list(last_move)
    if len(last_move) <> len(text):
        for char in last_move_chars:
            current_move_chars.remove(char)
        if current_move_chars[0] not in 'abcdefghijklmnopqrstuvwxyz':
            return 'Sorry, you added an invalid character.'
    else:
        misses = 0
        for char in last_move_chars:
            if char not in current_move_chars:
                misses += 1
            else:
                current_move_chars.remove(char)
        if misses == 1:
            if current_move_chars[0] not in 'abcdefghijklmnopqrstuvwxyz':
                return 'Sorry, you added an invalid character.'
        else:
            return 'Sorry you must either substitute a letter or add one.'
    
    # finally, check that it's a word.
    r = open(r'dict/%s.txt' % text[0])
    found = False
    while not found:
        h = r.readline()[:-1]
        if h == text:
            found = True
        if ord(h[1]) > ord(text[1]):
            break
    r.close()

    if not found:
        return 'Sorry, the word you entered is not valid.'
    else:
        for move in g.moves:
            if move[1] == text:
                return 'Sorry, that word has already been played.'
        g.make_move(p, text)
        print text + ' is valid'
        if len(last_move) == 6 and g.moves[-1][1] <> 'wf':
            g.add_chat(admin, 'The length is now 7 characters, you may now remove a character before adding a new one.')
        return 'good'

@route('/chat/:code/:text')
def chat(code, text):
    game_id = code[:8]
    player_id = code[8:]
    for game in games:
        g = game
        if g.id == game_id:
            break
    if g.id <> game_id:
        redirect('/game/' + game_id)
    
    for player in g.players:
        p = player
        if p.id == player_id:
            break
    if p.id <> player_id:
        redirect('/game/' + game_id)

    g.add_chat(p, text)

@route('/goto/:game_id/:player_pass')
def goto(game_id, player_pass):
    # find the game with that id_code
    for gam in games:
        g = gam
        if g.id == game_id:
            break
    # find the player with that pass
    for player in g.players:
        p = player
        if p.password == player_pass:
            break
    if p.password == player_pass:
        redirect('/game/' + g.id + p.id)
    else:
        redirect('/game/' + g.id)
    
@route('/register')
def register():
    output = '<html><head><title>Create a New Game</title></head><body>'
    output += '<table cellspacing="10"><tr><td colspan="2"><b>Game Info</b></td></tr>'
    output += '<tr><td>Name: </td><td><input type="text" size="20" id="game_name" /></td></tr>'
    output += '<tr><td>Password: </td><td><input type="password" size="20" id="game_password" /></td></tr>'
    output += '<tr><td colspan="2">&nbsp</td></tr>'
    output += '<tr><td colspan="2"><b>Profile Info</b></td></tr>'
    output += '<tr><td>Username: </td><td><input type="text" size="20" id="username" /></td></tr>'
    output += '<tr><td>Password: </td><td><input type="password" size="20" id="password" /></td></tr>'
    output += '<tr><td colspan="2"><input type="button" value="Submit" onclick="window.location=\'../create_game/\' + '
    output += 'escape(document.getElementById(\'game_name\').value) + \'/\' + escape(document.getElementById(\'game_password\').value) + '
    output += '\'/\' + escape(document.getElementById(\'username\').value) + \'/\' + escape(document.getElementById(\'password\').value)" />'
    output += '</td></tr></table></body></html>'
    return output

@route('/whatis')
def whatis():
    return '''
    <html>
<head>
<title>What is Wippen?</title>
<style type="text/css">
body {
    font-family: Georgia;
    font-size: 14px;
}

h1 {
    color: #333;
}

#container {
    width: 700px;
    border: 2px solid #000;
    background-color: #F0EAD6;
    padding: 20px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 40px;
    margin-bottom: 50px;
}

</style>
</head>
<body>
<div id="container">
<h1>What is Wippen?</h1>
<p>Wippen is a simple game I created in middle school several years ago with some friends. Since then 

it's become a great way to waste time during class, since all you need is a piece of paper and a pencil.</p>
<p>While the idea was not stolen, it may not be original, since it is a fairly <i>obvious</i> game. So don't be 

surprised if you've played a game like this before, or if you come across it one day by a different name.</p>
<p>Since I love the game so much, I took the time to make a webapp where people can play each other over the 

internet. Word validation and scoring is all automated.</p>

<h1>So how do I play?</h1>
<p>We'll talk about joining and creating rooms later. For now, let's focus on game mechanics.</p>
<p>Wippen starts with a randomly chosen two-letter word. Unfortunately, words like "ox" and "qi" lead to some 

pretty boring games. I'm working on this. Players take turns adding a letter to the word, forming a different 

word each time. If necessary, the player can rearrange the letters, but can only (and must) add one letter. The 

only rule to this is that you cannot simply add an s to make a word plural. For instance...</p>
<pre>
 : re
2: red
1: read
2: reads (XXX)
</pre>
<p>Is <b>not</b> okay. Here, player 2 went ahead and added an s to make "read" into "reads." Why is this not 

allowed? Because with each turn it becomes harder to think of a new word, and we want to keep it that way. It's 

also in place to keep word choices original. Keep in mind that if player 2 had rearranged the word "read" 

before adding an s, it would've been accepted (i.e. "dares" or "dears")</p>

<p>One other rule we have added is that once the word reaches <b>7 characters</b>, the player has the 

opportunity to remove a character before adding a different one. Essentially, the player may either add a 

letter, or just substitute one. This makes for much longer-lasting rounds and higher-scoring wins. Please note 

that a word can only be played <b>once</b> per round.</p>

<h1>So how do I win a round?</h1>
<p>If a player is unable to think of a word, he or she may enter "wf" (short for whiteflag: no quotes) to pass. 

If the other player then enters a valid move, that other player wins. If both players pass, the round ends in a 

draw, and the winning bonus points carry onto the next round.</p>

<h1>Scoring</h1>
<p>We're still working on this. For now, you get 1 point for winning, and 0 points for losing/drawing.</p>

<h1>Gameplay</h1>
<p>Here's an example of a real game between players "1" and "2."</p>
<pre>
 : is
2: his
1: this
2: shift
1: wf
2: shifty
Player 2 Wins!!
</pre>
<p>And here's another...</p>
<pre>
 : ka
1: kat
2: take
1: steak
2: staked
1: stalked
2: stalled
1: details
2: wf
1: derails
Player 1 wins!!
</pre>

<h1>This all sounds great, so how do I get started?</h1>
<p>Head on over to the <a href="../">Lobby</a> and join a game. To do so, you must enter the room's password, 

as decided by the room creator (we don't have public rooms yet). Then create a username and 

password. These are only temporary, and are in place so you can log into your game from anywhere. Alternatively, 

you can also make your own room!</p>
<p>Once a room has 2 players, the game can start. The "Administrator" (the room's robot) will take care of 

choosing a random starting word, as well as the scoring and notifying you when it's your turn. You can also 

chat on the right side of the page.</p>

<h1>Some more info</h1>
<p>Wippen is still being developed, and therefore is pretty ugly (but hey, it's functional). Some words are
missing, especially long words with added prefixes or suffixes, so we're working on that as well. If you do
catch any bugs, please report them to the email address listed below.</p>
<p>Wippen was developed by Jordan Scales using Python 2.7 and the <a href="http://bottle.paws.de">bottle</a> 

microweb framework. Feel free to send any comments or questions to scalesjordan (at) gmail.com. Enjoy!</p>
</div>
</body>
</html>'''

run(host='155.246.130.63', port='7777')
