from .UI import GameEntity;

class GUI:
	CLIENT        = None;
	EVENT_MANAGER = None;
	RENDER        = None;
	WINDOW        = None;

	# Easy.
	render = None;
	window = None;
	even_m = None;

	# Clock out.
	clock = None;

	def __init__(self, client, render_manager, event_manager):
		self.EVENT_MANAGER = event_manager;
		self.RENDER        = render_manager.getRender();
		self.CLIENT        = client;

		# Easy.
		self.render = self.RENDER;
		self.even_m = self.EVENT_MANAGER;

		# Init.
		self.render.init();

		# Init Window.
		self.WINDOW = self.render.display.set_mode((1280, 800), self.render.DOUBLEBUF);

		# Easy.
		self.window = self.WINDOW;

		# Config.
		self.render.display.set_caption(client.getClientName() + " - " + client.getClientUser());

		# Gay:
		self.Player = GameEntity.Entity(self.window, self.even_m, self.render, client.getClientUser(), 3432);

		self.clock = self.render.time.Clock();

		# Run.
		self.run();

	def setBackgroundColor(self, r, g, b):
		self.window.fill((190, 190, 190));

	def setFramePerSecond(self, summor):
		self.clock.tick(summor) / 1000;

	def run(self):
		while (self.even_m.getEvent("GameRunnig")):
			self.setBackgroundColor(190, 190, 190);
			self.setFramePerSecond(500);

			self.Player.render();
			self.Player.movement();

			if self.even_m.getEvent("K_DELETE"):
				self.Player.entity_life -= 0.50;

			if self.even_m.getEvent("K_w"):
				self.Player.entity_life = 10;

			self.mainloop();

	def mainloop(self):
		self.even_m.update(self.render, self.window);
		self.render.display.update();
