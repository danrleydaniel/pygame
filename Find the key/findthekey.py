import pygame

'''


		--- CRÉDITOS DOS SPRITES UTILIZADOS NESSE PROJETO: ---
		Protagonista e inimigo: https://opengameart.org/content/classic-hero-and-baddies-pack
		Chão e árvores: https://opengameart.org/content/beastlands
		Tijolos: https://opengameart.org/content/castle-exterior-tiles
		Disparo: http://freegameassets.blogspot.com/
		Ovo: https://opengameart.org/content/egg-0
		Mascote: https://opengameart.org/content/door-key-and-creatures
		Porta: https://opengameart.org/content/dungeon-door
		Chave: https://opengameart.org/content/key-icons


'''


WIDTH = 1000
HEIGHT = 600

pygame.init()

matriz = [
".................................................................................",
".................................................................................",
".................................................................................",
".................................................................................",
".................................................................................",
".................................................................................",
"............C....................................................................",
"..........TTTT...................................................................",
"...TTTT..........................................................................",
".................................................................................",
"...........M..........A..........M.....O...A......M...........................D..",
"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
]

screen = pygame.display.set_mode((WIDTH, HEIGHT),0)
BLOCK_W = WIDTH // 16
BLOCK_H = HEIGHT // 12

protagonista = pygame.image.load("sprites/main_hero.png.png")
piso = pygame.image.load("sprites/floor.png")
inimigo = pygame.image.load("sprites/enemy.png")
disparo = pygame.image.load("sprites/shoot.png")
mascote = pygame.image.load("sprites/mascot.png")
porta = pygame.image.load("sprites/door.png")
porta_fechada = pygame.image.load("sprites/door_locked.png")
tijolo = pygame.image.load("sprites/tile.png")
arvore = pygame.image.load("sprites/tree.png")
chave = pygame.image.load("sprites/key.png")
ovo = pygame.image.load("sprites/egg.png")

class Bloco(pygame.sprite.Sprite):
	def __init__(self, linha, coluna):
		pygame.sprite.Sprite.__init__(self)
		img_orig = piso
		self.image = pygame.transform.scale(img_orig, (BLOCK_W, BLOCK_H))
		x = coluna * BLOCK_W
		y = linha * BLOCK_H
		self.rect = pygame.Rect((x,y),(BLOCK_W,BLOCK_H))

class Tijolo(pygame.sprite.Sprite):
	def __init__(self, linha, coluna):
		pygame.sprite.Sprite.__init__(self)
		img_orig = tijolo
		self.image = pygame.transform.scale(img_orig, (BLOCK_W, BLOCK_H))
		x = coluna * BLOCK_W
		y = linha * BLOCK_H
		self.rect = pygame.Rect((x,y),(BLOCK_W, BLOCK_H))

class Arvore(pygame.sprite.Sprite):
	def __init__(self, linha, coluna):
		pygame.sprite.Sprite.__init__(self)
		img_orig = arvore
		self.image = pygame.transform.scale(img_orig, (BLOCK_W, BLOCK_H))
		x = coluna * BLOCK_W
		y = linha * BLOCK_H
		self.rect = pygame.Rect((x,y),(BLOCK_W, BLOCK_H))

class Chave(pygame.sprite.Sprite):
	def __init__(self, linha, coluna):
		pygame.sprite.Sprite.__init__(self)
		img_orig = chave
		self.image = pygame.transform.scale(img_orig, (BLOCK_W // 2, BLOCK_H // 2))
		x = coluna * BLOCK_W // 2
		y = linha * BLOCK_H // 2
		self.rect = pygame.Rect((x,y),(BLOCK_W // 2, BLOCK_H // 2))

class Porta(pygame.sprite.Sprite):
	def __init__(self, linha, coluna):
		pygame.sprite.Sprite.__init__(self)
		img_orig2 = porta_fechada
		self.image = pygame.transform.scale(img_orig2, (BLOCK_W, BLOCK_H))
		x = coluna * BLOCK_W
		y = linha * BLOCK_H
		self.rect = pygame.Rect((x,y),(BLOCK_W, BLOCK_H))

class Ovo(pygame.sprite.Sprite):
	def __init__(self, linha, coluna):
		pygame.sprite.Sprite.__init__(self)
		img_orig = ovo
		self.image = pygame.transform.scale(img_orig, (BLOCK_W, BLOCK_H))
		x = coluna * BLOCK_W
		y = linha * BLOCK_H
		self.rect = pygame.Rect((x,y),(BLOCK_W, BLOCK_H))


class Monster(pygame.sprite.Sprite):
	def __init__(self, linha, coluna):
		pygame.sprite.Sprite.__init__(self)
		img_orig = inimigo
		self.image = pygame.transform.scale(img_orig, (BLOCK_W, BLOCK_H))
		self.rect = pygame.Rect((coluna * BLOCK_W, linha * BLOCK_H), (BLOCK_W, BLOCK_H))
		self.vel_x = -0.009
		self.vel_y = 0

	def update(self, *args):
		self.rect.centerx += self.vel_x

class Disparo(pygame.sprite.Sprite):
	def __init__(self, personagem):
		pygame.sprite.Sprite.__init__(self)
		img_orig = disparo
		self.image = pygame.transform.scale(img_orig, (BLOCK_W // 2, BLOCK_H // 2))
		self.rect = pygame.Rect(personagem.rect.center, (BLOCK_W // 2, BLOCK_H // 2))
		self.vel_x = 6
		self.vel_y = 0

	def update(self, *args):
		self.rect.centerx += self.vel_x

class Protagonista(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		img_orig = protagonista
		self.image = pygame.transform.scale(img_orig, (BLOCK_W, BLOCK_H))
		self.rect = pygame.Rect((100, 100), (BLOCK_W, BLOCK_H))
		self.vel_x = 0
		self.vel_y = 0
		self.gravity = 0.009
		self.intencao_pos = list(self.rect.center)
		self.withthekey = False
		self.withamascot = False

	def mover_esquerda(self):
		self.vel_x = -2

	def mover_direita(self):
		self.vel_x = 2

	def pular(self):
		self.vel_y = -2

	def update(self, *args):
		self.vel_y += self.gravity
		self.intencao_pos[0] += self.vel_x
		self.intencao_pos[1] += self.vel_y

	def parar_horizontal(self):
		self.vel_x = 0

	def autorizar_movimento(self):
		self.rect.center = self.intencao_pos

	def rejeitar_movimento(self):
		self.intencao_pos = list(self.rect.center)

	def teste_colisao(self, grupo):
		aux = self.rect.center
		self.rect.center = self.intencao_pos
		if not pygame.sprite.spritecollide(main, grupo, False):
			self.autorizar_movimento()
		else:
			self.rect.center = aux
			self.vel_y = 0
			self.rejeitar_movimento()

	def pegar_chave(self):
		self.withthekey = True

	def pegar_mascote(self):
		self.withamascot = True

class Mascote(pygame.sprite.Sprite):
	def __init__(self, personagem):
		pygame.sprite.Sprite.__init__(self)
		img_orig = mascote
		self.image = pygame.transform.scale(img_orig, (BLOCK_W // 2, BLOCK_H // 2))
		self.rect = pygame.Rect(personagem.rect.center, (BLOCK_W // 2, BLOCK_H // 2))
		self.vel_x = 0
		self.vel_y = 0

	def update(self, personagem):
		self.rect.centerx = personagem.rect.centerx - 35

class Camera:
	def __init__(self, position, tamanho):
		self.window = pygame.Rect(position, tamanho)
		self.position = position
		self.offset_x = 0
		self.offset_y = 0
		self.clean_image = pygame.Surface(self.window.size)
		self.clean_image.fill((0,0,0))
		self.draw_area = pygame.Surface(self.window.size)

	def in_viewport(self, r):
		return self.window.colliderect(r)

	def move(self, pos):
		self.window.center = pos
		self.offset_x = self.window.x
		self.offset_y = self.window.y

	def start_drawing(self):
		self.draw_area.blit(self.clean_image, (0,0))

	def paint(self, tela):
		tela.blit(self.draw_area, self.position)
		pygame.draw.rect(tela, (255, 0, 0), (self.position, self.window.size), 3)

	def testa_colisao_mask(self, spr1, spr2):
		return pygame.sprite.collide_mask(spr1, spr2)

	def draw_group(self, group):
		for s in group:
			if self.in_viewport(s.rect):
				self.draw_area.blit(s.image, (s.rect.x - self.offset_x, s.rect.y - self.offset_y))

main = Protagonista()
heroes = pygame.sprite.Group(main)
blocks = pygame.sprite.Group()
enemies = pygame.sprite.Group()
shoots = pygame.sprite.Group()
keys = pygame.sprite.Group()
doors = pygame.sprite.Group()
trees = pygame.sprite.Group()
mascots = pygame.sprite.Group()
eggs = pygame.sprite.Group()

for linha, lin in enumerate(matriz):
	for coluna in range(0, 80):
		elemento = matriz[linha][coluna]
		if elemento == "P":
			pis = Bloco(linha, coluna)
			blocks.add(pis)
		elif elemento == "T":
			tijol = Tijolo(linha, coluna)
			blocks.add(tijol)
		elif elemento == "A":
			arvo = Arvore(linha, coluna)
			trees.add(arvo)
		elif elemento == "D":
			saida = Porta(linha, coluna)
			doors.add(saida)
		elif elemento == "C":
			chav = Chave(linha, coluna)
			keys.add(chav)
		elif elemento == "M":
			enemy = Monster(linha, coluna)
			enemies.add(enemy)
		elif elemento == "O":
			egg = Ovo(linha, coluna)
			eggs.add(egg)


cam = Camera((0,0),(WIDTH,HEIGHT))

while True:
	cam.start_drawing()

	cam.draw_group(blocks)

	cam.draw_group(heroes)

	cam.draw_group(enemies)

	cam.draw_group(shoots)

	cam.draw_group(keys)

	cam.draw_group(trees)

	cam.draw_group(doors)

	cam.draw_group(mascots)

	cam.draw_group(eggs)

	cam.paint(screen)
	pygame.display.update()

	heroes.update()
	shoots.update()
	enemies.update()

	if main.withamascot:
		mascots.update(main)

	main.teste_colisao(blocks)

	pygame.sprite.groupcollide(enemies, shoots, True, True)

	if pygame.sprite.groupcollide(heroes, keys, False, True):
		doors.image = pygame.transform.scale(porta, (BLOCK_W, BLOCK_H))
		main.pegar_chave()

	if pygame.sprite.groupcollide(heroes, enemies, True, False):
		print("Você perdeu :(")
		exit()

	if pygame.sprite.groupcollide(heroes, doors, False, False):
		if main.withthekey:
			print("Fim do jogo!")
			exit()

		else:
			print("Você precisa da chave para abrir essa porta")

	if pygame.sprite.groupcollide(heroes, eggs, False, True):
		mascot = Mascote(main)
		mascots.add(mascot)
		main.pegar_mascote()

	for tiro in shoots:
		if tiro.rect.centerx > (main.rect.centerx + 500):
			tiro.kill()
		
		if tiro.rect.centerx < (main.rect.centerx - 500):
			tiro.kill()

	cam.move(main.rect.center)

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit()

		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_RIGHT:
				main.mover_direita()

			if e.key == pygame.K_LEFT:
				main.mover_esquerda()

			if e.key == pygame.K_SPACE:
				main.pular()

			if e.key == pygame.K_x:
				tiro = Disparo(main)
				shoots.add(tiro)
				tiro.vel_x = 1

		if e.type == pygame.KEYUP:
			if e.key in [pygame.K_LEFT, pygame.K_RIGHT]:
				main.parar_horizontal()
