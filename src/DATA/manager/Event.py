class event:
	event_name  = None;
	event_state = None;

	def __init__(self, name, state):
		self.event_name  = name;
		self.event_state = state;

	def getName(self):
		return self.event_name;

	def setAction(self, action):
		self.event_state = action;

	def getAction(self):
		return self.event_state;
