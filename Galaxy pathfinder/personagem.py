class Personagem:
	def __init__(self, wx, wy, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.wx = wx
		self.wy = wy

class Alien:
	def __init__(self, wx, wy, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.wx = wx
		self.wy = wy
		self.upd = 1
		self.direc = 0

	def update(self, window_w):
		if self.x >= window_w - self.w:
			self.upd = -1
		elif self.x <= 150:
			self.upd = 1
		self.x += self.upd

		if self.direc == 2:
			self.direc = 0
		self.direc += 1
