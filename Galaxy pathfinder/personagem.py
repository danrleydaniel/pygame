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

	def update(self, window_w): #Recebe como parâmetro a largura da tela do jogo
		if self.x >= window_w - self.w:
			self.upd = -1 #Não permite que o alien passe da largura da janela do jogo
		elif self.x <= 150:
			self.upd = 1 #Não permite que o alien passe da largura da janela do jogo
		self.x += self.upd

		if self.direc == 2: #Tem relação com a lista pos_alien no código principal
			self.direc = 0 #Tem relação com a lista pos_alien no código principal
		self.direc += 1#Tem relação com a lista pos_alien no código principal
