import pygame
from random import randint

class Disparo(pygame.sprite.Sprite):
	def __init__(self, img, rect, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.upd = 1
		self.rect = rect
		self.image = img
		self.x = x
		self.y = y

	def update(self, *args):
		self.y += self.upd

def draw_group(win, group): #Desenha um grupo
	for s in group:
		win.blit(s.image, (s.x, s.y))

def is_colliding(obj1, obj2):
	if(obj1.y >= int(obj2.top)):
		return True

def is_colliding2(obj1, obj2):
	if(obj1.x < obj2.left + obj2.width and obj1.x + obj1.rect.width > obj2.left and obj1.y < obj2.top + obj2.height and obj1.y + obj1.rect.height > obj2.y):
		return True


relogio = pygame.time.Clock()
sprite_shoot = pygame.image.load("disparo/disparo.png")
shoots = pygame.sprite.Group()
shoot_rect = pygame.Rect(13, 13, 13, 13)


def main():
	pygame.init()
	tela = pygame.display.set_mode([500, 500])
	pygame.display.set_caption("Square Odissey")
	encerrar = False
	vidas = 10

	#CORES
	white = (255, 255, 255)
	blue = (0, 0, 139)
	green = (152, 251, 152)

	#RETÂNGULOS
	ret = pygame.Rect(0, 400, 500, 100)
	ret2 = pygame.Rect(220, 320, 50, 50)

	fonte = pygame.font.SysFont(pygame.font.get_default_font(), 20)


	tiro = Disparo(sprite_shoot, shoot_rect, randint(1, 499), 0)
	shoots.add(tiro)

	while not encerrar:
		relogio.tick(700)
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				encerrar = True

		if vidas == 0:
			encerrar = True

		if is_colliding(tiro, ret):
			tiro.kill()
			vidas -= 1
			tiro = Disparo(sprite_shoot, shoot_rect, randint(1, 499), 0)
			shoots.add(tiro)

		if is_colliding2(tiro, ret2):
			tiro.kill()
			tiro = Disparo(sprite_shoot, shoot_rect, randint(1, 499), 0)
			shoots.add(tiro)

		tela.fill(white)

		(ret2.left, ret2.top) = pygame.mouse.get_pos()
		ret2.left -= int(ret2.width/2)
		ret2.top -= int(ret2.height/2)

		pygame.draw.rect(tela, blue, ret)
		pygame.draw.rect(tela, green, ret2)

		text_vidas = fonte.render("VIDAS", 1, (0,0,0))
		text_numero = fonte.render(str(vidas), 1, (0,0,0))

		tela.blit(text_vidas, (25, 25))
		tela.blit(text_numero, (75, 25))

		shoots.update()
		draw_group(tela, shoots)
		pygame.display.update()

	pygame.quit()

main()
