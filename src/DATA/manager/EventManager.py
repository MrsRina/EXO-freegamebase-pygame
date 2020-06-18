from .Event import event;

class EVENT_MANAGER:
	EVENTS = {};

	def __init__(self):
		self.EVENTS = {};

		# Event start.
		self.createEvent("GameRunnig", "Game Start", True);

		# Keys.
		self.createEvent("K_BACKSPACE", "When press", False);
		self.createEvent("K_TAB", "When press", False);
		self.createEvent("K_CLEAR", "When press", False);
		self.createEvent("K_RETURN", "When press", False);
		self.createEvent("K_PAUSE", "When press", False);
		self.createEvent("K_ESCAPE", "When press", False);
		self.createEvent("K_SPACE", "When press", False);
		self.createEvent("K_EXCLAIM", "When press", False);
		self.createEvent("K_QUOTEDBL", "When press", False);
		self.createEvent("K_HASH", "When press", False);
		self.createEvent("K_DOLLAR", "When press", False);
		self.createEvent("K_AMPERSAND", "When press", False);
		self.createEvent("K_QUOTE", "When press", False);
		self.createEvent("K_LEFTPAREN", "When press", False);
		self.createEvent("K_RIGHTPAREN", "When press", False);
		self.createEvent("K_ASTERISK", "When press", False);
		self.createEvent("K_PLUS", "When press", False);
		self.createEvent("K_COMMA", "When press", False);
		self.createEvent("K_MINUS", "When press", False);
		self.createEvent("K_PERIOD", "When press", False);
		self.createEvent("K_SLASH", "When press", False);
		self.createEvent("K_0", "When press", False);
		self.createEvent("K_1", "When press", False);
		self.createEvent("K_2", "When press", False);
		self.createEvent("K_3", "When press", False);
		self.createEvent("K_4", "When press", False);
		self.createEvent("K_5", "When press", False);
		self.createEvent("K_6", "When press", False);
		self.createEvent("K_7", "When press", False);
		self.createEvent("K_8", "When press", False);
		self.createEvent("K_9", "When press", False);
		self.createEvent("K_COLON", "When press", False);
		self.createEvent("K_SEMICOLON", "When press", False);
		self.createEvent("K_LESS", "When press", False);
		self.createEvent("K_EQUALS", "When press", False);
		self.createEvent("K_GREATER", "When press", False);
		self.createEvent("K_QUESTION", "When press", False);
		self.createEvent("K_AT", "When press", False);
		self.createEvent("K_LEFTBRACKET", "When press", False);
		self.createEvent("K_BACKSLASH", "When press", False);
		self.createEvent("K_RIGHTBRACKET", "When press", False);
		self.createEvent("K_CARET", "When press", False);
		self.createEvent("K_UNDERSCORE", "When press", False);
		self.createEvent("K_BACKQUOTE", "When press", False);
		self.createEvent("K_a", "When pressed", False);
		self.createEvent("K_b", "When pressed", False);
		self.createEvent("K_c", "When pressed", False);
		self.createEvent("K_d", "When pressed", False);
		self.createEvent("K_e", "When pressed", False);
		self.createEvent("K_f", "When pressed", False);
		self.createEvent("K_g", "When pressed", False);
		self.createEvent("K_h", "When pressed", False);
		self.createEvent("K_i", "When pressed", False);
		self.createEvent("K_j", "When pressed", False);
		self.createEvent("K_k", "When pressed", False);
		self.createEvent("K_l", "When pressed", False);
		self.createEvent("K_m", "When pressed", False);
		self.createEvent("K_n", "When pressed", False);
		self.createEvent("K_o", "When pressed", False);
		self.createEvent("K_p", "When pressed", False);
		self.createEvent("K_q", "When pressed", False);
		self.createEvent("K_r", "When pressed", False);
		self.createEvent("K_s", "When pressed", False);
		self.createEvent("K_t", "When pressed", False);
		self.createEvent("K_u", "When pressed", False);
		self.createEvent("K_v", "When pressed", False);
		self.createEvent("K_w", "When pressed", False);
		self.createEvent("K_x", "When pressed", False);
		self.createEvent("K_y", "When pressed", False);
		self.createEvent("K_z", "When pressed", False);          
		self.createEvent("K_z", "When press", False);
		self.createEvent("K_DELETE", "When press", False);
		self.createEvent("K_KP0", "When press", False);
		self.createEvent("K_KP1", "When press", False);
		self.createEvent("K_KP2", "When press", False);
		self.createEvent("K_KP3", "When press", False);
		self.createEvent("K_KP4", "When press", False);
		self.createEvent("K_KP5", "When press", False);
		self.createEvent("K_KP6", "When press", False);
		self.createEvent("K_KP7", "When press", False);
		self.createEvent("K_KP8", "When press", False);
		self.createEvent("K_KP9", "When press", False);
		self.createEvent("K_KP_PERIOD", "When press", False);
		self.createEvent("K_KP_DIVIDE", "When press", False);
		self.createEvent("K_KP_MULTIPLY", "When press", False);
		self.createEvent("K_KP_MINUS", "When press", False);
		self.createEvent("K_KP_PLUS", "When press", False);
		self.createEvent("K_KP_ENTER", "When press", False);
		self.createEvent("K_KP_EQUALS", "When press", False);
		self.createEvent("K_UP", "When press", False);
		self.createEvent("K_DOWN", "When press", False);
		self.createEvent("K_RIGHT", "When press", False);
		self.createEvent("K_LEFT", "When press", False);
		self.createEvent("K_INSERT", "When press", False);
		self.createEvent("K_HOME", "When press", False);
		self.createEvent("K_END", "When press", False);
		self.createEvent("K_PAGEUP", "When press", False);
		self.createEvent("K_PAGEDOWN", "When press", False);
		self.createEvent("K_F1", "When press", False);
		self.createEvent("K_F2", "When press", False);
		self.createEvent("K_F3", "When press", False);
		self.createEvent("K_F4", "When press", False);
		self.createEvent("K_F5", "When press", False);
		self.createEvent("K_F6", "When press", False);
		self.createEvent("K_F7", "When press", False);
		self.createEvent("K_F8", "When press", False);
		self.createEvent("K_F9", "When press", False);
		self.createEvent("K_F10", "When press", False);
		self.createEvent("K_F11", "When press", False);
		self.createEvent("K_F12", "When press", False);
		self.createEvent("K_F13", "When press", False);
		self.createEvent("K_F14", "When press", False);
		self.createEvent("K_F15", "When press", False);
		self.createEvent("K_NUMLOCK", "When press", False);
		self.createEvent("K_CAPSLOCK", "When press", False);
		self.createEvent("K_SCROLLOCK", "When press", False);
		self.createEvent("K_RSHIFT", "When press", False);
		self.createEvent("K_LSHIFT", "When press", False);
		self.createEvent("K_RCTRL", "When press", False);
		self.createEvent("K_LCTRL", "When press", False);
		self.createEvent("K_RALT", "When press", False);
		self.createEvent("K_LALT", "When press", False);
		self.createEvent("K_RMETA", "When press", False);
		self.createEvent("K_LMETA", "When press", False);
		self.createEvent("K_LSUPER", "When press", False);
		self.createEvent("K_RSUPER", "When press", False);
		self.createEvent("K_MODE", "When press", False);
		self.createEvent("K_HELP", "When press", False);
		self.createEvent("K_PRINT", "When press", False);
		self.createEvent("K_SYSREQ", "When press", False);
		self.createEvent("K_BREAK", "When press", False);
		self.createEvent("K_MENU", "When press", False);
		self.createEvent("K_POWER", "When press", False);
		self.createEvent("K_EURO", "When press", False);

	def createEvent(self, name, when, state):
		self.postEvent(event(name, state));

	def getEvents(self):
		return self.EVENTS;

	def postEvent(self, event_):
		self.EVENTS[event_.getName()] = event_;

	def getEventClazz(self, name):
		return self.EVENTS[name];

	def getEvent(self, name):
		return self.EVENTS[name].getAction();

	def update(self, render, window):
		event_pressed = render.key.get_pressed();

		self.getEventClazz("K_BACKSPACE").setAction(event_pressed[render.K_BACKSPACE]);
		self.getEventClazz("K_TAB").setAction(event_pressed[render.K_TAB]);
		self.getEventClazz("K_CLEAR").setAction(event_pressed[render.K_CLEAR]);
		self.getEventClazz("K_RETURN").setAction(event_pressed[render.K_RETURN]);
		self.getEventClazz("K_PAUSE").setAction(event_pressed[render.K_PAUSE]);
		self.getEventClazz("K_ESCAPE").setAction(event_pressed[render.K_ESCAPE]);
		self.getEventClazz("K_SPACE").setAction(event_pressed[render.K_SPACE]);
		self.getEventClazz("K_EXCLAIM").setAction(event_pressed[render.K_EXCLAIM]);
		self.getEventClazz("K_QUOTEDBL").setAction(event_pressed[render.K_QUOTEDBL]);
		self.getEventClazz("K_HASH").setAction(event_pressed[render.K_HASH]);
		self.getEventClazz("K_DOLLAR").setAction(event_pressed[render.K_DOLLAR]);
		self.getEventClazz("K_AMPERSAND").setAction(event_pressed[render.K_AMPERSAND]);
		self.getEventClazz("K_QUOTE").setAction(event_pressed[render.K_QUOTE]);
		self.getEventClazz("K_LEFTPAREN").setAction(event_pressed[render.K_LEFTPAREN]);
		self.getEventClazz("K_RIGHTPAREN").setAction(event_pressed[render.K_RIGHTPAREN]);
		self.getEventClazz("K_ASTERISK").setAction(event_pressed[render.K_ASTERISK]);
		self.getEventClazz("K_PLUS").setAction(event_pressed[render.K_PLUS]);
		self.getEventClazz("K_COMMA").setAction(event_pressed[render.K_COMMA]);
		self.getEventClazz("K_MINUS").setAction(event_pressed[render.K_MINUS]);
		self.getEventClazz("K_PERIOD").setAction(event_pressed[render.K_PERIOD]);
		self.getEventClazz("K_SLASH").setAction(event_pressed[render.K_SLASH]);
		self.getEventClazz("K_0").setAction(event_pressed[render.K_0]);
		self.getEventClazz("K_1").setAction(event_pressed[render.K_1]);
		self.getEventClazz("K_2").setAction(event_pressed[render.K_2]);
		self.getEventClazz("K_3").setAction(event_pressed[render.K_3]);
		self.getEventClazz("K_4").setAction(event_pressed[render.K_4]);
		self.getEventClazz("K_5").setAction(event_pressed[render.K_5]);
		self.getEventClazz("K_6").setAction(event_pressed[render.K_6]);
		self.getEventClazz("K_7").setAction(event_pressed[render.K_7]);
		self.getEventClazz("K_8").setAction(event_pressed[render.K_8]);
		self.getEventClazz("K_9").setAction(event_pressed[render.K_9]);
		self.getEventClazz("K_COLON").setAction(event_pressed[render.K_COLON]);
		self.getEventClazz("K_SEMICOLON").setAction(event_pressed[render.K_SEMICOLON]);
		self.getEventClazz("K_LESS").setAction(event_pressed[render.K_LESS]);
		self.getEventClazz("K_EQUALS").setAction(event_pressed[render.K_EQUALS]);
		self.getEventClazz("K_GREATER").setAction(event_pressed[render.K_GREATER]);
		self.getEventClazz("K_QUESTION").setAction(event_pressed[render.K_QUESTION]);
		self.getEventClazz("K_AT").setAction(event_pressed[render.K_AT]);
		self.getEventClazz("K_LEFTBRACKET").setAction(event_pressed[render.K_LEFTBRACKET]);
		self.getEventClazz("K_BACKSLASH").setAction(event_pressed[render.K_BACKSLASH]);
		self.getEventClazz("K_RIGHTBRACKET").setAction(event_pressed[render.K_RIGHTBRACKET]);
		self.getEventClazz("K_CARET").setAction(event_pressed[render.K_CARET]);
		self.getEventClazz("K_UNDERSCORE").setAction(event_pressed[render.K_UNDERSCORE]);
		self.getEventClazz("K_BACKQUOTE").setAction(event_pressed[render.K_BACKQUOTE]);
		self.getEventClazz("K_a").setAction(event_pressed[render.K_a]);
		self.getEventClazz("K_b").setAction(event_pressed[render.K_b]);
		self.getEventClazz("K_c").setAction(event_pressed[render.K_c]);
		self.getEventClazz("K_d").setAction(event_pressed[render.K_d]);
		self.getEventClazz("K_e").setAction(event_pressed[render.K_e]);
		self.getEventClazz("K_f").setAction(event_pressed[render.K_f]);
		self.getEventClazz("K_g").setAction(event_pressed[render.K_g]);
		self.getEventClazz("K_h").setAction(event_pressed[render.K_h]);
		self.getEventClazz("K_i").setAction(event_pressed[render.K_i]);
		self.getEventClazz("K_j").setAction(event_pressed[render.K_j]);
		self.getEventClazz("K_k").setAction(event_pressed[render.K_k]);
		self.getEventClazz("K_l").setAction(event_pressed[render.K_l]);
		self.getEventClazz("K_m").setAction(event_pressed[render.K_m]);
		self.getEventClazz("K_n").setAction(event_pressed[render.K_n]);
		self.getEventClazz("K_o").setAction(event_pressed[render.K_o]);
		self.getEventClazz("K_p").setAction(event_pressed[render.K_p]);
		self.getEventClazz("K_q").setAction(event_pressed[render.K_q]);
		self.getEventClazz("K_r").setAction(event_pressed[render.K_r]);
		self.getEventClazz("K_s").setAction(event_pressed[render.K_s]);
		self.getEventClazz("K_t").setAction(event_pressed[render.K_t]);
		self.getEventClazz("K_u").setAction(event_pressed[render.K_u]);
		self.getEventClazz("K_v").setAction(event_pressed[render.K_v]);
		self.getEventClazz("K_w").setAction(event_pressed[render.K_w]);
		self.getEventClazz("K_x").setAction(event_pressed[render.K_x]);
		self.getEventClazz("K_y").setAction(event_pressed[render.K_y]);
		self.getEventClazz("K_z").setAction(event_pressed[render.K_z]);
		self.getEventClazz("K_DELETE").setAction(event_pressed[render.K_DELETE]);
		self.getEventClazz("K_KP0").setAction(event_pressed[render.K_KP0]);
		self.getEventClazz("K_KP1").setAction(event_pressed[render.K_KP1]);
		self.getEventClazz("K_KP2").setAction(event_pressed[render.K_KP2]);
		self.getEventClazz("K_KP3").setAction(event_pressed[render.K_KP3]);
		self.getEventClazz("K_KP4").setAction(event_pressed[render.K_KP4]);
		self.getEventClazz("K_KP5").setAction(event_pressed[render.K_KP5]);
		self.getEventClazz("K_KP6").setAction(event_pressed[render.K_KP6]);
		self.getEventClazz("K_KP7").setAction(event_pressed[render.K_KP7]);
		self.getEventClazz("K_KP8").setAction(event_pressed[render.K_KP8]);
		self.getEventClazz("K_KP9").setAction(event_pressed[render.K_KP9]);
		self.getEventClazz("K_KP_PERIOD").setAction(event_pressed[render.K_KP_PERIOD]);
		self.getEventClazz("K_KP_DIVIDE").setAction(event_pressed[render.K_KP_DIVIDE]);
		self.getEventClazz("K_KP_MULTIPLY").setAction(event_pressed[render.K_KP_MULTIPLY]);
		self.getEventClazz("K_KP_MINUS").setAction(event_pressed[render.K_KP_MINUS]);
		self.getEventClazz("K_KP_PLUS").setAction(event_pressed[render.K_KP_PLUS]);
		self.getEventClazz("K_KP_ENTER").setAction(event_pressed[render.K_KP_ENTER]);
		self.getEventClazz("K_KP_EQUALS").setAction(event_pressed[render.K_KP_EQUALS]);
		self.getEventClazz("K_UP").setAction(event_pressed[render.K_UP]);
		self.getEventClazz("K_DOWN").setAction(event_pressed[render.K_DOWN]);
		self.getEventClazz("K_RIGHT").setAction(event_pressed[render.K_RIGHT]);
		self.getEventClazz("K_LEFT").setAction(event_pressed[render.K_LEFT]);
		self.getEventClazz("K_INSERT").setAction(event_pressed[render.K_INSERT]);
		self.getEventClazz("K_HOME").setAction(event_pressed[render.K_HOME]);
		self.getEventClazz("K_END").setAction(event_pressed[render.K_END]);
		self.getEventClazz("K_PAGEUP").setAction(event_pressed[render.K_PAGEUP]);
		self.getEventClazz("K_PAGEDOWN").setAction(event_pressed[render.K_PAGEDOWN]);
		self.getEventClazz("K_F1").setAction(event_pressed[render.K_F1]);
		self.getEventClazz("K_F2").setAction(event_pressed[render.K_F2]);
		self.getEventClazz("K_F3").setAction(event_pressed[render.K_F3]);
		self.getEventClazz("K_F4").setAction(event_pressed[render.K_F4]);
		self.getEventClazz("K_F5").setAction(event_pressed[render.K_F5]);
		self.getEventClazz("K_F6").setAction(event_pressed[render.K_F6]);
		self.getEventClazz("K_F7").setAction(event_pressed[render.K_F7]);
		self.getEventClazz("K_F8").setAction(event_pressed[render.K_F8]);
		self.getEventClazz("K_F9").setAction(event_pressed[render.K_F9]);
		self.getEventClazz("K_F10").setAction(event_pressed[render.K_F10]);
		self.getEventClazz("K_F11").setAction(event_pressed[render.K_F11]);
		self.getEventClazz("K_F12").setAction(event_pressed[render.K_F12]);
		self.getEventClazz("K_F13").setAction(event_pressed[render.K_F13]);
		self.getEventClazz("K_F14").setAction(event_pressed[render.K_F14]);
		self.getEventClazz("K_F15").setAction(event_pressed[render.K_F15]);
		self.getEventClazz("K_NUMLOCK").setAction(event_pressed[render.K_NUMLOCK]);
		self.getEventClazz("K_CAPSLOCK").setAction(event_pressed[render.K_CAPSLOCK]);
		self.getEventClazz("K_SCROLLOCK").setAction(event_pressed[render.K_SCROLLOCK]);
		self.getEventClazz("K_RSHIFT").setAction(event_pressed[render.K_RSHIFT]);
		self.getEventClazz("K_LSHIFT").setAction(event_pressed[render.K_LSHIFT]);
		self.getEventClazz("K_RCTRL").setAction(event_pressed[render.K_RCTRL]);
		self.getEventClazz("K_LCTRL").setAction(event_pressed[render.K_LCTRL]);
		self.getEventClazz("K_RALT").setAction(event_pressed[render.K_RALT]);
		self.getEventClazz("K_LALT").setAction(event_pressed[render.K_LALT]);
		self.getEventClazz("K_RMETA").setAction(event_pressed[render.K_RMETA]);
		self.getEventClazz("K_LMETA").setAction(event_pressed[render.K_LMETA]);
		self.getEventClazz("K_LSUPER").setAction(event_pressed[render.K_LSUPER]);
		self.getEventClazz("K_RSUPER").setAction(event_pressed[render.K_RSUPER]);
		self.getEventClazz("K_MODE").setAction(event_pressed[render.K_MODE]);
		self.getEventClazz("K_HELP").setAction(event_pressed[render.K_HELP]);
		self.getEventClazz("K_PRINT").setAction(event_pressed[render.K_PRINT]);
		self.getEventClazz("K_SYSREQ").setAction(event_pressed[render.K_SYSREQ]);
		self.getEventClazz("K_BREAK").setAction(event_pressed[render.K_BREAK]);
		self.getEventClazz("K_MENU").setAction(event_pressed[render.K_MENU]);
		self.getEventClazz("K_POWER").setAction(event_pressed[render.K_POWER]);
		self.getEventClazz("K_EURO").setAction(event_pressed[render.K_EURO]);

		for events in render.event.get():
			if events.type is render.QUIT:
				self.getEventClazz("GameRunnig").setAction(False);