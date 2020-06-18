class Entity:
	# Managers.
	e_manager = None;
	r_manager = None;

	# Settings.
	window = None;

	# Positions.
	x = 0;
	y = 0;

	# HitBox Sizes.
	w = 0;
	h = 0;

	# Colors.
	r = 0;
	g = 0;
	b = 0;

	# Configs.
	entity_tag = "null";
	entity_pin = 0000;

	entity_life  = 0;
	entity_state = 0;

	def __init__(self, window, e_Manager, r_Manager, tag, pin):
		self.e_manager = e_Manager;
		self.r_manager = r_Manager;

		self.entity_tag = tag;
		self.entity_pin = pin;

		self.window = window;

		self.x = 0; self.y = 0; self.w = 10; self.h = 10;

		self.entity_life  = 10;

		self.e_manager.createEvent(self.getName() + "Spawn", "Spawn entity", False);
		self.e_manager.createEvent(self.getName() + "Living", "Spawn living", True);

	def getName(self):
		return (self.entity_tag + str(self.entity_pin));

	def setX(self, x):
		self.x = x;

	def getX(self):
		return self.x;

	def setY(self, y):
		self.y = y;

	def getY(self):
		return self.y;

	def setW(self, w):
		self.w = w;

	def getW(self):
		return self.w;

	def setH(self, h):
		self.h = h;

	def getH(self):
		return self.h;

	def draw(self):
		if self.e_manager.getEvent(self.getName() + "Living") and self.e_manager.getEvent(self.getName() + "Spawn"):
			self.r_manager.draw.rect(self.window, (self.r, self.g, self.b), [self.x, self.y, self.w, self.h]);

	def movement(self):
		if (self.e_manager.getEvent("K_RIGHT")):
			self.x += 0.50;

		if (self.e_manager.getEvent("K_LEFT")):
			self.x -= 0.50;

		if (self.e_manager.getEvent("K_UP")):
			self.y -= 0.50;

		if (self.e_manager.getEvent("K_DOWN")):
			self.y += 0.50;

	def render(self):
		if self.entity_life == 0:
			self.e_manager.getEventClazz(self.getName() + "Spawn").setAction(False);
			self.e_manager.getEventClazz(self.getName() + "Living").setAction(False);
		elif self.entity_life > 0:
			if self.e_manager.getEventClazz(self.getName() + "Spawn").getAction() != True:
				self.e_manager.getEventClazz(self.getName() + "Spawn").setAction(True);

			self.e_manager.getEventClazz(self.getName() + "Living").setAction(True);

		self.draw();
