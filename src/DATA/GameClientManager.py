class GameClient:
	CLIENT_NAME = None;
	CLIENT_VERS = None;
	CLIENT_USER = None;

	def __init__(self):
		self.CLIENT_NAME = "null";
		self.CLIENT_VERS = "0.0";
		self.CLIENT_USER = "NoName";

	def setClientName(self, name):
		self.CLIENT_NAME = name;

	def getClientName(self):
		return self.CLIENT_NAME;

	def setClientVers(self, vers):
		self.CLIENT_VERS = vers;

	def getClientVers(self):
		return self.CLIENT_VERS;

	def setClientUser(self, nick):
		self.CLIENT_USER = nick;

	def getClientUser(self):
		return self.CLIENT_USER;