import botlib
 
# Create a new class for our bot, extending the Bot class from botlib
class ElectroBot(botlib.Bot):
    def __init__(self, server, channel, nick, password=None):
        botlib.Bot.__init__(self, server, 6667, channel, nick)
 
        # Send nickserv password if availible
        if password != None:
            self.protocol.privmsg("nickserv", "identify" % password)
 
    def __actions__(self):
        botlib.Bot.__actions__(self)
 
        # Create a Hello World responder/command
        if botlib.check_found(self.data, "!hello"):
            # Get the senders username
            username = self.get_username()
 
            # Send user a message in response
            self.protocol.privmsg(self.channel, "Hello %s!" % username)
 
if __name__ == "__main__":
    # Create new instance of our bot and run it
    HelloWorldBot("irc.wyldryde.org", "#maddog39", "HelloWorldBot").run()
