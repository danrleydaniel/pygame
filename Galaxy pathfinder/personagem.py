class Personagem:
	def __init__(self, wx, wy, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.wx = wx
		self.wy = wy
		self.posicao = "idle"
		self.com_a_gasolina = False
		self.dentro_do_foguete = False

	def pegar_gasolina(self):
		self.com_a_gasolina = True

	def entrar_no_foguete(self):
		self.dentro_do_foguete = True

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
		self.vivo = True

	def update(self, window_w): #Recebe como parâmetro a largura da tela do jogo
		if self.vivo:
			if self.x >= window_w - self.w:
				self.upd = -1 #Não permite que o alien passe da largura da janela do jogo
			elif self.x <= 150:
				self.upd = 1 #Não permite que o alien passe da largura da janela do jogo
			self.x += self.upd

			if self.direc == 2: #Tem relação com a lista pos_alien no código principal
				self.direc = 0 #Tem relação com a lista pos_alien no código principal
			self.direc += 1 #Tem relação com a lista pos_alien no código principal
		else:
			self.upd = 0
			self.direc = 3

	def matar(self):
		self.vivo = False
