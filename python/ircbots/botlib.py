#+---------------------------------------------+
#| PyBotlib 1.0
#+---------------------------------------------+
#| Written by Alec Hussey
#| Copyright (C) 2008 MadSoft
#| Website: www.madsoft.org
#| License: Public Domain
#+---------------------------------------------+

from socket import *
import sys, time, random, string, threading

check_found = lambda s, k: (True if s.find(k) > -1 else False)

class Protocol:
	def __init__(self, server, port=6667):
		self.connection = socket(AF_INET, SOCK_STREAM)
		self.connection.connect((server, port))
	
	def send(self, message):
		datasent = 0
		message += "\n"
		
		"""
		Continue sending chunks of the message until
		the entire message has been sent to the server
		"""
		while datasent < len(message):
			sent = self.connection.send(message)
			if sent == 0:
				raise RuntimeError, "Connection reset by peer."
			else:
				datasent += sent
	
	def recv(self):
		data = str()
		
		"""
		Continue recieving data from the server until
		we have recieved the end of the message
		"""
		while data.find("\r") == -1:
			chunk = self.connection.recv(512)
			if chunk == None:
				raise RuntimeError, "Connection reset by peer."
			else:
				data += chunk
		
		return data
	
	def join(self, channel):
		self.send("JOIN %s" % channel)
	
	def notice(self, nickname, text):
		self.send("NOTICE %s :%s" % (nickname, text))
	
	def privmsg(self, reciever, message):
		self.send("PRIVMSG %s :%s" % (reciever, message))
	
	def identify(self, username):
		self.send("USER %s localhost localhost :%s" % (username, username))
		self.send("NICK %s" % username)
	
	def whois(self, nickname):
		self.send("WHOIS %s" % nickname)
		
		# Pull down who is data from server
		data = str()
		while not check_found(data, "End of WHOIS"):
			data += self.recv()
		
		return data
	
	def disconnect(self, message="Disconnected"):
		self.send("QUIT :%s" % message)
		#time.sleep(5.0)
		#self.connection.shutdown(SHUT_RDWR)
		#self.connection.close()

class Bot(threading.Thread):
	def __init__(self, server, port, channel, nick):
		# Intialize threading
		threading.Thread.__init__(self)
		
		# Initialize IRC protocol
		self.protocol = Protocol(server, port)
		self.protocol.identify(nick)
		
		# Initialize class variables
		self.server = server
		self.port = port
		self.channel = channel
		self.nick = nick
		self.data = None
		self.joined = False
	
	def __actions__(self):
		# Recieve incoming data from server
		self.data = self.protocol.recv()
		
		# Check for and respond to PING requests
		if check_found(self.data, "PING"):
			ping = self.data.rstrip().split()
			self.protocol.send("PONG %s" % ping[1])
			
			# Check to see if the client has joined their
			# specirfied channel yet, if not then join it
			if not self.joined:
				self.protocol.join(self.channel)
				self.joined = True
	
	def get_args(self):
		return self.data.split()[4:]
	
	def get_username(self):
		return self.data.split("!")[0].strip(":")
	
	def get_hostname(self):
		return self.data.split("!")[1].split(" ")[0]
	
	def run(self):
		# Start loop and perform user defined actions
		while True:
			self.__actions__()

class BotManager:
	def __init__(self):
		"""
		NOTE:
		Not exactly sure why I made this a dictionary so
		let me sit on it for a while.
		"""
		self.botlist = {}
		
	def __length__(self):
		return len(self.botlist)
	
	def add(self, bot):
		# Append the given bot to the list
		nextbot = len(self.botlist) + 1
		self.botlist[nextbot] = bot
	
	def remove(self, botid):
		# Disconnect and delete the given bot number
		self.botlist[botid].disconnect()
		del self.botlist[botid]
	
	def remove_all(self):
		# Loop through bots disconnecting each
		for (botid, botobject) in self.botlist:
			botobject.disconnect()
		
		# Clear entire bot list
		self.botlist.clear()
	
	def send_all(self, messsage):
		# Loop through all bots sending each the given message
		for botid in self.botlist.keys():
			self.botlist[botid].protocol.send(message)
	
	def recv_all(self):
		data = []
		
		# Recieve data from all bots in list
		for botid in self.botlist.keys():
			data.append(self.botlist[botid].protocol.recv())
		
		return data
