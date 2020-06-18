import pygame as pg;

class RENDER_MANAGER:
	pygame = None;

	def __init__(self):
		self.pygame = pg;

	def getRender(self):
		return self.pygame;