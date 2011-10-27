import botlib
from time import *
from random import *

###TEMPLATE FOR POSTING
"""
if botlib.check_found(self.data, "TEXT"):
                self.protocol.privmsg(self.channel, MESSAGE)
"""

# Create a new class for our bot, extending the Bot class from botlib

dictn = '!botinfo, what is love?, electrobot, !time, daft punk, !help, never gonna give you up, blogs, stupid bot, !entertain, !tell a joke'

class ElectroBot(botlib.Bot):
    
    def __init__(self, server, channel, nick, password=None):
        botlib.Bot.__init__(self, server, 6667, channel, nick)
 
        # Send nickserv password if availible
        if password != None:
            self.protocol.privmsg("nickserv", "identify %s" % password)
            
    def __actions__(self):
        botlib.Bot.__actions__(self)
        username = self.get_username()

        if username != "Electro-Bot":
            # Create a Hello World responder/command
            if botlib.check_found(self.data, "hello"):
                self.protocol.privmsg(self.channel, "Hello %s!" % username)

            if botlib.check_found(self.data, "hey"):
                self.protocol.privmsg(self.channel, "Hello %s!" % username)
                
            if botlib.check_found(self.data, "!botinfo"):
                self.protocol.privmsg(self.channel, "Electro-Bot is an IRC bot created by Jordan Scales (ilictronix). For a list of commands, type !help")

            if botlib.check_found(self.data, "what is love"):
                self.protocol.privmsg(self.channel, "Baby don't hurt me...")

            if botlib.check_found(self.data, "electro-bot"):
                self.protocol.privmsg(self.channel, "Did you call me, %s?" % (username))

            if botlib.check_found(self.data, "!time"):
                self.protocol.privmsg(self.channel, "The current time is %s:%s:%s EST" % (localtime()[3], localtime()[4], localtime()[5]))    

            if botlib.check_found(self.data, "daft punk"):
                self.protocol.privmsg(self.channel, "OH OH OH DID I HEAR MY FAVORITE ARTISTS!?!?")

            if botlib.check_found(self.data, "where are you"):
                self.protocol.privmsg(self.channel, "I'm in Middletown, NJ!")

            if botlib.check_found(self.data, "!help"):
                self.protocol.privmsg(self.channel, "My current dictionary includes: %s" % (dictn))

            if botlib.check_found(self.data, "never gonna give you up"):
                self.protocol.privmsg(self.channel, "never gonna let you down...")

            if botlib.check_found(self.data, "dumb"):
                self.protocol.privmsg(self.channel, "YOU'RE DUMB, FATTY")

            if botlib.check_found(self.data, "gay"):
                self.protocol.privmsg(self.channel, "Looks like someone is hiding something...")

            if botlib.check_found(self.data, "rofl"):
                self.protocol.privmsg(self.channel, "Oh how I love a good laugh...")

            if botlib.check_found(self.data, " blog"):
                self.protocol.privmsg(self.channel, "Speaking of blogs, maybe you should check out http://ilictronix.com!")

            if botlib.check_found(self.data, "tits"):
                self.protocol.privmsg(self.channel, ":-D")

            if botlib.check_found(self.data, "nigger"):
                self.protocol.privmsg(self.channel, "You ignorant little whore!")

            if botlib.check_found(self.data, ":-("):
                self.protocol.privmsg(self.channel, "Why so blue?")

            if botlib.check_found(self.data, "thanks"):
                self.protocol.privmsg(self.channel, "You're welcome %s!"%(username))

            if botlib.check_found(self.data, "stupid bot"):
                self.protocol.privmsg(self.channel, "Shut the fuck up you little fucker")

            if botlib.check_found(self.data, "h/o"):
                self.protocol.privmsg(self.channel, "Yes, sir")

            if botlib.check_found(self.data, "pwned"):
                self.protocol.privmsg(self.channel, "l0lz own3d into next julyyy")

            if botlib.check_found(self.data, "hi "):
                self.protocol.privmsg(self.channel, "Howdy %s!" % username)

            if botlib.check_found(self.data, "yes."):
                self.protocol.privmsg(self.channel, "Oh, okay then.")

            if botlib.check_found(self.data, "no."):
                self.protocol.privmsg(self.channel, ":( why not?")

            if botlib.check_found(self.data, "!entertain"):
                self.protocol.privmsg(self.channel, "Hello ladies and gents, anyone care for a chardonnay?")

            if botlib.check_found(self.data, "woot"):
                self.protocol.privmsg(self.channel, "w00000t")

            if botlib.check_found(self.data, "!tell a joke"):
                temp = randint(1,10)
                joke = ''
                if temp>8:
                    joke="Whats the most confusing holiday in Harlem? Father's Day!"
                elif temp>7:
                    joke="Women's rights."
                elif temp>6:
                    joke="What do you call a mexican riding a bike? A criminal."
                elif temp>5:
                    joke="Why did the chicken cross the road? To get to the other side!"
                elif temp>4:
                    joke="No."
                elif temp>3:
                    joke="Sorry, I'm not feeling very funny right about now."
                elif temp>2:
                    joke="What do you call a mexican parking garage? A bike rack."
                elif temp>1:
                    joke="Ilictronix is the worst blog ever!"
                self.protocol.privmsg(self.channel, joke)

            if botlib.check_found(self.data, "g2g"):
                self.protocol.privmsg(self.channel, "Goodbye %s!" % username)

            if botlib.check_found(self.data, "bye"):
                self.protocol.privmsg(self.channel, "See ya later %s!" % username)
                
if __name__ == "__main__":
    # Create new instance of our bot and run it
    ElectroBot("irc.geekshed.net", "#ilictronix", "Electro-Bot", "he7302jd33d").run()
