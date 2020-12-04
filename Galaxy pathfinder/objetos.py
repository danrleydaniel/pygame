import pygame

class Tiro(pygame.sprite.Sprite):
	def __init__(self, dire, img, personagem, sr):
		pygame.sprite.Sprite.__init__(self)
		self.upd = -2
		if personagem.posicao == "left":
			self.upd = -2
		elif personagem.posicao == "right":
			self.upd = 2
		self.rect = sr
		self.image = img
		self.x = personagem.x
		self.y = personagem.y

	def update(self, *args):
		self.x += self.upd

class Gasolina(pygame.sprite.Sprite):
	def __init__(self, img, gas_x, gas_y, sr):
		pygame.sprite.Sprite.__init__(self)
		self.rect = sr
		self.image = img
		self.x = gas_x
		self.y = gas_y
		self.gerado = False

	def gerar(self):
		self.gerado = True

	def destruir(self):
		self.gerado = False
