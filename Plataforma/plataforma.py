import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()

#Essa matriz representa a plataforma. Cada "." é um espaço vazio. Cada "P" é um espaço ocupado pelo piso.
matriz = [
	".................................................................................",
	".................................................................................",
	".................................................................................",
	".................................................................................",
	".................................................................................",
	".................................................................................",
	"...PPPPP.........................................................................",
	".................................................................................",
	".................................................................................",
	".......PPPPP.....................................................................",
	".............................M...................................................",
	"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
]



screen = pygame.display.set_mode((WIDTH, HEIGHT),0) #Pinta a plataforma
BLOCK_W = WIDTH // 16 # ---\ Esses valores representam o tamanho de cada
BLOCK_H = HEIGHT // 12 #---/ bloquinho.

caracteres = pygame.image.load("Sprite/Owlet_Monster_Attack1_4.png") #Carrega a imagem do personagem
basictiles = pygame.image.load("Sprite/Nature_environment_01.png") #Carrega a imagem dos blocos do cenário
monster = pygame.image.load("Sprite/IMGBIN_rpg-maker-mv-rpg-maker-vx-rpg-maker-xp-sprite-role-playing-video-game-png_byiLnpng.png") #Carrega a imagem do monstro
shoot = pygame.image.load("Sprite/pm_1.png") #Carrega a imagem do disparo

#Classe que define o bolo
class Bloco(pygame.sprite.Sprite):
	def __init__(self, linha, coluna):
		pygame.sprite.Sprite.__init__(self)
		img_orig = basictiles
		self.image = pygame.transform.scale(img_orig, (BLOCK_W, BLOCK_H))
		x = coluna * BLOCK_W
		y = linha * BLOCK_H
		self.rect = pygame.Rect((x,y),(BLOCK_W, BLOCK_H))

#Classe que define o mosntro
class Monstro(pygame.sprite.Sprite):
	def __init__(self, linha, coluna):
		pygame.sprite.Sprite.__init__(self)
		monster_orig = monster
		self.image = pygame.transform.scale(monster_orig, (BLOCK_W, BLOCK_H))
		self.rect = pygame.Rect((coluna * BLOCK_W, linha * BLOCK_H), (BLOCK_W, BLOCK_H))
		self.vel_x = 0
		self.vel_y = 0

	def update(self, *args):
		self.rect.centerx += self.vel_x

#Classe que define o tiro
class Disparo(pygame.sprite.Sprite):
	def __init__(self, personagem):
		pygame.sprite.Sprite.__init__(self)
		shoot_orig = shoot
		self.image = pygame.transform.scale(shoot_orig, (BLOCK_W // 2, BLOCK_H // 2))
		self.rect = pygame.Rect(personagem.rect.center, (BLOCK_W // 2, BLOCK_H // 2))
		self.vel_x = 6
		self.vel_y = 0

	def update(self, *args):
		self.rect.centerx += self.vel_x

#Classe que traz os atributos do protagonista
class Boy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		boy_original = caracteres.subsurface((32 * 0, 32 * 0), (32, 32)) #Recorta apenas o sprite que eu quero da imagem carregada na linha 30. Para entender melhor isso, é bom assistir: https://youtu.be/trOnGGsKtjg?t=1426
		self.image = pygame.transform.scale(boy_original, (BLOCK_W, BLOCK_H)) #Redimensionaliza o sprite, para que não fique muito pequeno
		self.rect = pygame.Rect((100, 100), (BLOCK_W, BLOCK_H))
		self.vel_x = 0
		self.vel_y = 0
		self.gravidade = 0.009
		self.intencao_pos = list(self.rect.center)

	def mover_esquerda(self):
		self.vel_x = -1 #Faz o personagem andar para a esquerda, diminuindo 1 do eixo X

	def mover_direita(self):
		self.vel_x = 1 #Faz o personagem andar para a direita, aumentando 1 no eixo X

	def pular(self):
		self.vel_y = -2 #Faz o personagem pular, diminuindo 1 no eixo Y

	def update(self, *args):
		self.vel_y += self.gravidade # A velocidade com a qual o personagem cai, aumentando valores no eixo Y, é definida pelo atributo gravidade
		self.intencao_pos[0] += self.vel_x # Operação que faz o personagem ir para a direita ou esquerda
		self.intencao_pos[1] += self.vel_y # Operação que faz o personagem pular

	def parar_horizontal(self):
		self.vel_x = 0 #Quando o personagem não está indo nem para a direita, nem para a esquerda

	def autorizar_movimento(self):
		self.rect.center = self.intencao_pos #Define se o personagem pode se movimentar

	def rejeita_movimento(self):
		self.intencao_pos = list(self.rect.center) #Define se o personagem não pode se movimentar

	def teste_colisao(self, grupo): #Faz o teste de colisão do personagem com os blocos do cenário
		temp = self.rect.center
		self.rect.center = self.intencao_pos
		if not pygame.sprite.spritecollide(boy, blocos, False):
			self.autorizar_movimento()
		else:
			self.rect.center = temp
			self.vel_y = 0
			self.rejeita_movimento()


#Classe que faz a câmera acompanhar o personagem
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


boy = Boy() #Criando um objeto da classe Boy, que contém as informações do protagonista
herois = pygame.sprite.Group(boy) #Adiciona o protagonista a um grupo de sprites, conhecido como "heróis"
blocos = pygame.sprite.Group() #Grupo de blocos do cenário
inimigos = pygame.sprite.Group() #Grupo de inimigos
tiros = pygame.sprite.Group() #Grupo de disparos

for linha, lin in enumerate(matriz): #Percorre a matriz, para definir o cenário da plataforma
	for coluna in range(0, 80):
		elemento = matriz[linha][coluna]
		if elemento == "P":
			bloco = Bloco(linha, coluna)
			blocos.add(bloco)
		elif elemento == "M":
			enemy = Monstro(linha, coluna)
			inimigos.add(enemy)

cam = Camera((0,0),(WIDTH,HEIGHT)) #Cria a câmera, com o tamanho da tela

#Laço principal rotina do Pygame
while True:

	#Aciona os métodos da câmera
	cam.start_drawing()
	
	#Pinta os quadradinhos na plataforma conforme definido na matriz
	cam.draw_group(blocos)

	#Desenha o grupo de heróis, ao qual o protagonista faz parte
	cam.draw_group(herois)

	#Desenha os inimigos
	cam.draw_group(inimigos)

	#Desenha os tiros
	cam.draw_group(tiros)

	cam.paint(screen)
	pygame.display.update()

	#Calcula regras
	herois.update()
	tiros.update()
	boy.teste_colisao(blocos)

	pygame.sprite.groupcollide(inimigos, tiros, True, True) #Quando o tiro atinge o inimigo, tanto o tiro quanto o personagem desaparecem

	for tiro in tiros: #Quando o tiro afasta-se muito do personagem, desaparece
		if tiro.rect.centerx > (boy.rect.centerx + 500):
			tiro.kill()

		if tiro.rect.centerx < (boy.rect.centerx - 500):
			tiro.kill()

	cam.move(boy.rect.center) #Move a câmera segundo a posição do personagem


	#Processa eventos
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit()

		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_RIGHT:
				boy.mover_direita() #O personagem vai para a direita, quando aperta-se a tecla da seta direita no teclado

			if e.key == pygame.K_LEFT:
				boy.mover_esquerda() #O personagem vai para a esquerda, quando aperta-se a tecla da seta esquerda no teclado

			if e.key == pygame.K_SPACE:
				boy.pular() #O personagem pula quando aperta-se o espaço no teclado

			if e.key == pygame.K_x:
				tiro = Disparo(boy) #O personagem dispara quando aperta a tecla "X"
				tiros.add(tiro)
				tiro.vel_x = 1
		if e.type == pygame.KEYUP:
			if e.key in [pygame.K_LEFT, pygame.K_RIGHT]:
				boy.parar_horizontal() #Quando nem a tecla da seta direita, nem da esquerda estão apertadas, o personagem para
