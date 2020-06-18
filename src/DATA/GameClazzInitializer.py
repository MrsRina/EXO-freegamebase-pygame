from .GameClientManager import GameClient;
from .GUI.GameGUI       import GUI;
from .manager           import RENDER_MANAGER, EVENT_MANAGER;

from . import NAME, VERSION, AUTHOR, V_STATE, USER, GameDevUtil;

class GameClazz:
	CLIENT = None;

	event_initialized = False;

	def __init__(self, tag):
		self.CLIENT = GameClient();

		self.CLIENT.setClientName(NAME);
		self.CLIENT.setClientVers(VERSION);
		self.CLIENT.setClientUser(AUTHOR); # self.CLIENT.setClientUser(USER);

		self.event_initialized = True;

		if (self.is_initialized()):
			GameDevUtil.print_client(self.CLIENT.getClientName(), self.CLIENT.getClientVers(), AUTHOR, self.CLIENT.getClientUser(), " ");

	def is_initialized(self):
		return self.event_initialized;

	def run(self):
		GUI(self.CLIENT, RENDER_MANAGER(), EVENT_MANAGER());